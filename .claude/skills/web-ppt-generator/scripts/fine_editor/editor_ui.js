(() => {
  const stage = document.getElementById('stage');
  const slideLabel = document.getElementById('slideLabel');
  const prevBtn = document.getElementById('prevSlide');
  const nextBtn = document.getElementById('nextSlide');
  const saveBtn = document.getElementById('saveBtn');
  const bundleBtn = document.getElementById('bundleBtn');
  const qaBtn = document.getElementById('qaBtn');
  const finalizeBtn = document.getElementById('finalizeBtn');
  const deselectBtn = document.getElementById('deselectBtn');
  const statusMsg = document.getElementById('statusMsg');
  const resultBanner = document.getElementById('resultBanner');
  const resultPath = document.getElementById('resultPath');
  const resultQa = document.getElementById('resultQa');

  const inspectorEmpty = document.getElementById('inspectorEmpty');
  const inspectorFields = document.getElementById('inspectorFields');
  const inspectorMulti = document.getElementById('inspectorMulti');
  const fContent = document.getElementById('fContent');
  const fX = document.getElementById('fX');
  const fY = document.getElementById('fY');
  const fieldSize = document.getElementById('fieldSize');
  const fW = document.getElementById('fW');
  const fH = document.getElementById('fH');
  const fieldContent = document.getElementById('fieldContent');
  const fieldImage = document.getElementById('fieldImage');
  const fImageFile = document.getElementById('fImageFile');

  const qaPanel = document.getElementById('qaPanel');
  const qaOutput = document.getElementById('qaOutput');
  document.getElementById('closeQa').addEventListener('click', () => { qaPanel.hidden = true; });

  const undoBtn = document.getElementById('undoBtn');
  const redoBtn = document.getElementById('redoBtn');
  const resetSlideBtn = document.getElementById('resetSlideBtn');

  let doc = null, win = null, slides = [], currentIndex = 0;
  let selected = null; // { type: 'text'|'image', el } — 단일 선택(또는 다중 선택 중 "대표")
  let multiSelection = []; // { type, el }[] — 길이 2 이상일 때만 "다중 선택 모드"로 취급
  let dirty = false;
  let handleEls = [];
  const CORNERS = ['nw', 'ne', 'sw', 'se'];
  const SIDES = ['w', 'e']; // Text 전용 — Width만 바꾸는 좌우 변 핸들(Height는 그대로 유지)
  const pristineSlideHTML = new Map(); // slide data-index -> innerHTML at Fine Editing 시작 시점

  // ---- Undo/Redo History (Editor 내부 메모리에만 존재, 저장 전까지 디스크 미반영) ----
  // history의 각 항목은 items 배열이다: [{el, before, after}, ...]. 단일 요소 편집은 길이 1,
  // 여러 요소를 함께 드래그한 경우(다중 선택 이동)는 길이 N — 그래도 "1회 작업"으로 취급해
  // 한 번의 undo/redo로 전체가 함께 되돌아간다.
  let history = [];
  let historyIndex = -1;

  function pushHistory(items) {
    if (!items || !items.length) return;
    history = history.slice(0, historyIndex + 1);
    history.push(items);
    historyIndex = history.length - 1;
    updateUndoRedoButtons();
  }

  function applyHistoryState(el, state) {
    if (state.left !== undefined) el.style.left = state.left + 'px';
    if (state.top !== undefined) el.style.top = state.top + 'px';
    if (state.width !== undefined) el.style.width = state.width + 'px';
    if (state.height !== undefined) el.style.height = state.height + 'px';
    if (state.textContent !== undefined) el.textContent = state.textContent;
    if (state.src !== undefined) el.setAttribute('src', state.src);
  }

  function afterHistoryChange(items) {
    markDirty();
    const first = items[0].el;
    const slide = slideOf(first);
    if (!slide || !slide.classList.contains('is-active')) return; // 다른 슬라이드는 선택 상태로 만들지 않음
    if (items.length > 1) {
      restoreMultiSelection(items.map((it) => ({ type: it.el.tagName === 'IMG' ? 'image' : 'text', el: it.el })));
    } else {
      multiSelection = [];
      select({ type: first.tagName === 'IMG' ? 'image' : 'text', el: first });
    }
  }

  function undo() {
    if (historyIndex < 0) return;
    const items = history[historyIndex];
    items.forEach((it) => applyHistoryState(it.el, it.before));
    historyIndex--;
    updateUndoRedoButtons();
    afterHistoryChange(items);
    setStatus('실행 취소했습니다.');
  }

  function redo() {
    if (historyIndex >= history.length - 1) return;
    historyIndex++;
    const items = history[historyIndex];
    items.forEach((it) => applyHistoryState(it.el, it.after));
    updateUndoRedoButtons();
    afterHistoryChange(items);
    setStatus('다시 실행했습니다.');
  }

  function updateUndoRedoButtons() {
    undoBtn.disabled = historyIndex < 0;
    redoBtn.disabled = historyIndex >= history.length - 1;
  }

  function isTypingTarget(el) {
    // Text 내용 textarea만 네이티브(브라우저 기본) undo를 보존한다. X/Y/W/H 숫자 입력칸은
    // "타이핑 세션"이라 부를 만한 게 없어(값 하나 바뀌면 change로 즉시 커밋됨), 여기서
    // Ctrl+Z를 막으면 포커스가 그 입력칸에 남아있는 채로는 우리 History Undo가 전혀
    // 동작하지 않는 것처럼 보이는 문제가 있었다 — 그 경우까지 우리 Undo가 그대로 먹도록 한다.
    return el === fContent;
  }

  function handleUndoRedoKeydown(e) {
    // 슬라이드 안에서 Text를 직접 편집(contenteditable) 중일 때도 네이티브 undo를 보존한다.
    if (isTypingTarget(document.activeElement)) return;
    if (editingTextEl) return;
    const key = e.key.toLowerCase();
    if ((e.ctrlKey || e.metaKey) && !e.shiftKey && key === 'z') { e.preventDefault(); undo(); }
    else if ((e.ctrlKey || e.metaKey) && (key === 'y' || (key === 'z' && e.shiftKey))) { e.preventDefault(); redo(); }
  }
  window.addEventListener('keydown', handleUndoRedoKeydown);
  undoBtn.addEventListener('click', undo);
  redoBtn.addEventListener('click', redo);

  // ---- 좌표를 slide 경계 안(최소 일부는 보이도록)으로 제한 ----
  const MIN_VISIBLE_PX = 24;
  function clampPosition(x, y, w, h, slideW, slideH) {
    const minX = MIN_VISIBLE_PX - w, maxX = slideW - MIN_VISIBLE_PX;
    const minY = MIN_VISIBLE_PX - h, maxY = slideH - MIN_VISIBLE_PX;
    return {
      x: Math.min(Math.max(x, minX), Math.max(minX, maxX)),
      y: Math.min(Math.max(y, minY), Math.max(minY, maxY)),
    };
  }

  function setStatus(msg, isError) {
    statusMsg.textContent = msg;
    statusMsg.style.color = isError ? '#ff6b6b' : '';
  }

  function markDirty() {
    dirty = true;
    setStatus('저장하지 않은 변경사항이 있습니다.');
  }

  window.addEventListener('beforeunload', (e) => {
    if (dirty) { e.preventDefault(); e.returnValue = ''; }
  });

  stage.addEventListener('load', onStageLoad);

  function onStageLoad() {
    doc = stage.contentDocument;
    win = stage.contentWindow;
    slides = Array.from(doc.querySelectorAll('.slide'));
    currentIndex = slides.findIndex((s) => s.classList.contains('is-active'));
    if (currentIndex < 0) currentIndex = 0;
    updateSlideLabel();
    attachInteractionHandlers();
    doc.addEventListener('keydown', handleUndoRedoKeydown);
    pristineSlideHTML.clear();
    slides.forEach((s) => pristineSlideHTML.set(s.dataset.index, s.innerHTML));
    history = [];
    historyIndex = -1;
    updateUndoRedoButtons();
    clearSelection();
    setStatus('불러오기 완료.');
  }

  function updateSlideLabel() {
    slideLabel.textContent = `${slides.length ? currentIndex + 1 : 0} / ${slides.length}`;
  }

  function showSlide(i) {
    if (!slides.length) return;
    i = Math.max(0, Math.min(slides.length - 1, i));
    slides.forEach((s, idx) => s.classList.toggle('is-active', idx === i));
    currentIndex = i;
    updateSlideLabel();
    clearSelection();
  }
  prevBtn.addEventListener('click', () => showSlide(currentIndex - 1));
  nextBtn.addEventListener('click', () => showSlide(currentIndex + 1));

  resetSlideBtn.addEventListener('click', () => {
    if (!slides.length) return;
    const slide = slides[currentIndex];
    const idx = slide.dataset.index;
    if (!pristineSlideHTML.has(idx)) return;
    const ok = window.confirm(
      `현재 슬라이드(${currentIndex + 1}번)를 Fine Editing 시작 당시 상태로 되돌립니다.\n` +
      '이 작업은 실행 취소(Undo)로 되돌릴 수 없습니다. 계속할까요?'
    );
    if (!ok) return;
    clearSelection();
    slide.innerHTML = pristineSlideHTML.get(idx);
    // 슬라이드를 통째로 교체했으므로, 그 안의 이전 요소를 참조하던 history 항목은
    // 더 이상 유효하지 않다 — 혼란을 피하기 위해 전체 history를 함께 초기화한다.
    history = [];
    historyIndex = -1;
    updateUndoRedoButtons();
    markDirty();
    setStatus(`슬라이드 ${currentIndex + 1}번을 초기 상태로 되돌렸습니다.`);
  });

  // ---- 선택 대상 판별 (qa_render.py의 "직접 텍스트를 가진 leaf" 정의와 동일한 기준) ----
  function hasDirectText(el) {
    for (const child of el.childNodes) {
      if (child.nodeType === 3 && child.textContent.trim().length > 0) return true;
    }
    return false;
  }

  function findEditableTarget(startEl) {
    const slide = startEl.closest && startEl.closest('.slide');
    if (!slide) return null;
    let el = startEl;
    while (el && el !== slide.parentElement) {
      if (el.tagName === 'IMG') return { type: 'image', el };
      if (hasDirectText(el)) return { type: 'text', el };
      if (el === slide) break;
      el = el.parentElement;
    }
    return null;
  }

  function attachInteractionHandlers() {
    doc.body.addEventListener('click', (e) => {
      if (e.target.closest('[data-fe-handle]')) return;
      const found = findEditableTarget(e.target);

      // 지금 편집(더블클릭 진입) 중인 Text가 있는데 다른 곳을 클릭했다면 먼저 편집을 종료한다.
      if (editingTextEl && (!found || found.el !== editingTextEl)) {
        exitTextEditMode();
      }
      // 편집 중인 Text 내부 클릭(캐럿 이동 등)은 선택 로직을 다시 타지 않는다.
      if (found && editingTextEl === found.el) return;

      if (found && (e.ctrlKey || e.metaKey || e.shiftKey)) {
        e.preventDefault();
        toggleMultiSelect(found);
        return;
      }

      // multiSelection을 여기서 미리 비우지 않는다 — select()/clearSelection()이 각자
      // "지금 multiSelection에 들어있는 요소들"의 fe-selected 클래스를 제거한 뒤에 배열을
      // 비운다. 여기서 먼저 비우면 그 클린업 루프가 빈 배열을 도는 셈이 되어, 이전에
      // 복수 선택돼 있던 요소들의 파란 테두리가 지워지지 않고 화면에 그대로 남는다.
      if (found) {
        e.preventDefault();
        select(found);
      } else {
        clearSelection();
      }
    }, true);

    doc.body.addEventListener('dblclick', (e) => {
      if (e.target.closest('[data-fe-handle]')) return;
      const found = findEditableTarget(e.target);
      if (found && found.type === 'text') {
        e.preventDefault();
        enterTextEditMode(found.el, e);
      }
    });

    // 브라우저 기본 이미지 드래그(고스트 이미지)가 우리 커스텀 드래그와 충돌하지 않도록 막는다.
    doc.body.addEventListener('dragstart', (e) => e.preventDefault());

    doc.body.addEventListener('pointerdown', (e) => {
      if (e.target.closest('[data-fe-handle]')) return;
      const group = multiSelection.length > 1 ? multiSelection : (selected ? [selected] : []);
      if (!group.length) return;
      const hit = group.find((s) => s.el === e.target || s.el.contains(e.target));
      if (!hit || hit.el.isContentEditable) return; // 편집 모드 중에는 드래그를 시작하지 않는다
      if (group.length > 1) startGroupDrag(e, group);
      else startDrag(e);
    });
  }

  function clearSelection() {
    if (editingTextEl) exitTextEditMode();
    if (selected) selected.el.classList.remove('fe-selected');
    multiSelection.forEach((s) => s.el.classList.remove('fe-selected'));
    multiSelection = [];
    selected = null;
    removeHandles();
    inspectorEmpty.hidden = false;
    inspectorFields.hidden = true;
    inspectorMulti.hidden = true;
  }
  deselectBtn.addEventListener('click', clearSelection);

  function select(target) {
    if (editingTextEl && editingTextEl !== target.el) exitTextEditMode();
    if (selected) selected.el.classList.remove('fe-selected');
    multiSelection.forEach((s) => s.el.classList.remove('fe-selected'));
    multiSelection = [];
    selected = target;
    // "처음 선택된 시점"의 실제 렌더링 X/Y/W/H를 곧바로 고정 기준값으로 확보한다 — 이후
    // 이동/편집 과정에서 부모 flex/grid의 재배치나 텍스트 재줄바꿈에 영향받지 않게 하기 위함.
    ensureAbsolute(selected.el);
    ensureSelectionStyle();
    selected.el.classList.add('fe-selected');
    inspectorEmpty.hidden = true;
    inspectorFields.hidden = false;
    inspectorMulti.hidden = true;
    fieldContent.hidden = target.type !== 'text';
    fieldImage.hidden = target.type !== 'image';
    // Width/Height는 Text/Image 공통으로 보여준다 — Text Box도 Image처럼 직접 크기 조절이
    // 가능해야 한다(자동으로 얼려둔 폭이 부족해 원치 않는 위치에서 줄바꿈되는 문제의 해결책).
    fieldSize.hidden = false;
    if (target.type === 'text') fContent.value = target.el.textContent;
    syncInspectorFromEl();
    renderHandles();
  }

  // ---- 다중 선택 (Ctrl/Shift + Click) ----
  function toggleMultiSelect(found) {
    if (editingTextEl) exitTextEditMode();
    ensureAbsolute(found.el); // 다중 선택에 합류하는 요소도 즉시 위치/크기를 고정한다
    if (selected && !multiSelection.some((s) => s.el === selected.el)) {
      multiSelection.push(selected);
    }
    const idx = multiSelection.findIndex((s) => s.el === found.el);
    if (idx >= 0) {
      multiSelection.splice(idx, 1);
      found.el.classList.remove('fe-selected');
    } else {
      ensureSelectionStyle();
      multiSelection.push(found);
      found.el.classList.add('fe-selected');
    }

    if (multiSelection.length === 0) {
      clearSelection();
    } else if (multiSelection.length === 1) {
      const only = multiSelection[0];
      multiSelection = [];
      select(only);
    } else {
      selected = multiSelection[multiSelection.length - 1];
      removeHandles();
      inspectorEmpty.hidden = true;
      inspectorFields.hidden = true;
      inspectorMulti.hidden = false;
      inspectorMulti.textContent =
        `${multiSelection.length}개 선택됨 — 하나를 드래그하면 전체가 같은 방향·거리로 함께 이동합니다 ` +
        '(개별 상대 위치·간격은 그대로 유지). 내용/크기 수정은 하나만 선택해서 진행하세요.';
    }
  }

  function restoreMultiSelection(items) {
    if (selected) selected.el.classList.remove('fe-selected');
    multiSelection.forEach((s) => s.el.classList.remove('fe-selected'));
    multiSelection = items;
    ensureSelectionStyle();
    multiSelection.forEach((s) => s.el.classList.add('fe-selected'));
    selected = multiSelection[multiSelection.length - 1];
    removeHandles();
    inspectorEmpty.hidden = true;
    inspectorFields.hidden = true;
    inspectorMulti.hidden = false;
    inspectorMulti.textContent = `${multiSelection.length}개 선택됨 (Undo/Redo로 복원됨).`;
  }

  function ensureSelectionStyle() {
    if (doc.getElementById('fe-style')) return;
    const style = doc.createElement('style');
    style.id = 'fe-style';
    style.textContent = `
      .fe-selected { outline: 2px solid #4f7dfc !important; outline-offset: 2px; cursor: move; touch-action: none; }
      .fe-selected.fe-editing { outline-color: #22b25f !important; cursor: text; }
      [data-fe-handle] { position: absolute; width: 10px; height: 10px; background: #4f7dfc;
        border: 1px solid #fff; border-radius: 2px; z-index: 99999; cursor: nwse-resize; touch-action: none; }
    `;
    doc.head.appendChild(style);
  }

  // ---- 좌표 처리 ----
  function slideOf(el) { return el.closest('.slide'); }

  function ensureAbsolute(el) {
    const slide = slideOf(el);
    if (!slide) return;
    if (win.getComputedStyle(slide).position === 'static') slide.style.position = 'relative';

    if (el.style.left) {
      // 이미 얼려둔 요소 — margin 리셋만 멱등하게 보장하고 끝낸다.
      el.style.margin = '0';
      return;
    }

    const cs = win.getComputedStyle(el);
    const wasPositioned = cs.position === 'absolute' || cs.position === 'fixed';

    // position을 absolute로 바꾸기 *전에* 지금 실제 렌더링된 위치·크기를 전부 측정해 둔다.
    // width/height까지 반드시 여기서(포지션 전환 전에) 얼려야 한다 — position:absolute로
    // 바뀌는 순간 텍스트는 width가 auto(shrink-to-fit)로 재계산되어 줄바꿈이 바뀔 수 있고,
    // top:auto 상태에서는 margin이 static-position 계산에 이미 녹아 있어 이 시점의
    // offsetLeft/offsetTop이 "지금 실제로 보이는 위치"를 정확히 담고 있기 때문이다(Text 위치
    // 이동은 위치만 바꿔야 하고 기존 Box 크기·줄바꿈은 그대로 유지해야 한다는 요구사항).
    const left0 = Math.round(el.offsetLeft);
    const top0 = Math.round(el.offsetTop);
    const width0 = Math.round(el.offsetWidth);
    const height0 = Math.round(el.offsetHeight);

    // el을 position:absolute로 바꾸면 그 순간 el은 flex/grid/일반 문서 흐름에서 완전히
    // 빠진다 — 흐름이 차지하던 자리(마진 박스)가 사라지므로, 같은 부모 아래 있던 다른
    // sibling들이 그 빈 자리를 메우며 재배치(reflow)된다(첨부 화면에서 아래 Text가 위로
    // 당겨져 겹친 원인). el이 빠지기 *직전*에 지금 el이 차지하던 만큼의 자리를 대신
    // 지키는 투명 placeholder를 el 자리에 심어 두면, sibling 입장에서는 여전히 같은
    // 크기의 박스가 그 자리에 남아있는 것으로 보여 전혀 움직이지 않는다. (사후에 흐트러진
    // sibling을 다시 원위치로 보정하는 방식이 아니라,애초에 흐트러질 원인 자체를 없앤다.)
    if (!wasPositioned) {
      const placeholder = doc.createElement('span');
      placeholder.setAttribute('data-fe-placeholder', '');
      placeholder.style.display = cs.display === 'inline' ? 'inline-block' : cs.display;
      placeholder.style.boxSizing = 'border-box';
      placeholder.style.width = width0 + 'px';
      placeholder.style.height = height0 + 'px';
      placeholder.style.marginTop = cs.marginTop;
      placeholder.style.marginRight = cs.marginRight;
      placeholder.style.marginBottom = cs.marginBottom;
      placeholder.style.marginLeft = cs.marginLeft;
      placeholder.style.flex = cs.flex;
      placeholder.style.flexShrink = cs.flexShrink;
      placeholder.style.alignSelf = cs.alignSelf;
      placeholder.style.justifySelf = cs.justifySelf;
      placeholder.style.gridColumn = cs.gridColumn;
      placeholder.style.gridRow = cs.gridRow;
      placeholder.style.visibility = 'hidden';
      placeholder.style.pointerEvents = 'none';
      el.parentNode.insertBefore(placeholder, el);
    }

    if (!wasPositioned) el.style.position = 'absolute';
    // margin은 항상 0으로 통일한다 — position:absolute에서 top/left는 margin 바깥쪽(마진 박스)
    // 기준이므로, margin이 남아있으면 우리가 쓰는 left/top 값에 그 margin이 그대로 더해져
    // 어긋난다. 위에서 이미 현재 위치를 측정해 뒀으므로, margin을 0으로 만들고 그 값을
    // 그대로 적용해도 시각적으로 전혀 움직이지 않는다.
    el.style.margin = '0';
    el.style.left = left0 + 'px';
    el.style.top = top0 + 'px';
    el.style.width = width0 + 'px';
    el.style.height = height0 + 'px';
  }

  // el.style.left/top는 항상 offsetParent 기준이다(.slide 자신이 아닐 수 있음). Inspector에
  // 보여주는 "슬라이드 안에서의 위치"나 경계 클램프는 .slide 기준이어야 하므로, 이 델타를
  // 구해 두 좌표계를 서로 변환한다.
  function offsetParentDelta(el) {
    const parent = el.offsetParent;
    const slide = slideOf(el);
    if (!parent || parent === slide) return { x: 0, y: 0 };
    const pr = parent.getBoundingClientRect();
    const sr = slide.getBoundingClientRect();
    return { x: pr.left - sr.left, y: pr.top - sr.top };
  }

  // .slide 기준 좌표(실제 렌더링 결과를 항상 getBoundingClientRect로 읽으므로 offsetParent가
  // 무엇이든 정확하다) — Inspector 표시값과 경계 클램프 판정에 사용한다.
  function getXY(el) {
    const slide = slideOf(el);
    const sr = slide.getBoundingClientRect();
    const r = el.getBoundingClientRect();
    return {
      x: Math.round(r.left - sr.left), y: Math.round(r.top - sr.top),
      w: Math.round(r.width), h: Math.round(r.height),
    };
  }

  // .slide 기준 좌표(slideX, slideY)를 이 요소의 실제 CSS 기준(offsetParent)으로 변환해
  // el.style.left/top에 쓴다. 반환값은 실제로 적용된 offsetParent 기준 값 — history에는
  // 이 값을 그대로 저장해야 undo/redo가 el.style.left/top에 직접 대입해도 정확하다.
  function writeSlidePosition(el, slideX, slideY) {
    const d = offsetParentDelta(el);
    const left = Math.round(slideX - d.x);
    const top = Math.round(slideY - d.y);
    el.style.left = left + 'px';
    el.style.top = top + 'px';
    return { left, top };
  }

  function syncInspectorFromEl() {
    if (!selected) return;
    const { x, y, w, h } = getXY(selected.el);
    fX.value = x; fY.value = y;
    fW.value = w; fH.value = h;
  }

  // ---- 슬라이드 위에서 Text 직접 수정 (더블클릭) ----
  // contenteditable은 편집 중에만 임시로 붙이고, 편집이 끝나면 즉시 제거한다 — 저장되는
  // HTML에는 이 속성이 남지 않는다(serializeCleanHTML에서도 한 번 더 방어적으로 정리한다).
  let editingTextEl = null;
  let editingTextBefore = null;
  let editingInputHandler = null;

  function enterTextEditMode(el, e) {
    if (editingTextEl === el) return;
    if (editingTextEl) exitTextEditMode();
    ensureAbsolute(el); // Box 크기를 먼저 고정해, 타이핑 중 부모 재배치로 줄바꿈이 바뀌지 않게 한다
    multiSelection = [];
    select({ type: 'text', el });

    editingTextEl = el;
    editingTextBefore = el.textContent;
    el.setAttribute('contenteditable', 'true');
    el.classList.add('fe-editing');

    editingInputHandler = () => {
      fContent.value = el.textContent;
      markDirty();
    };
    el.addEventListener('input', editingInputHandler);
    el.addEventListener('keydown', onEditingKeydown);

    el.focus();
    // 클릭한 지점 근처에 캐럿을 두려는 best-effort (지원 안 하면 조용히 무시)
    try {
      if (doc.caretRangeFromPoint) {
        const range = doc.caretRangeFromPoint(e.clientX, e.clientY);
        if (range) {
          const sel = win.getSelection();
          sel.removeAllRanges();
          sel.addRange(range);
        }
      }
    } catch (err) { /* 캐럿 위치는 부가 기능일 뿐, 실패해도 편집 자체는 계속된다 */ }

    setStatus('Text 직접 편집 중 — 다른 곳을 클릭하면 종료됩니다.');
  }

  function onEditingKeydown(e) {
    if (e.key === 'Escape') { e.preventDefault(); exitTextEditMode(); }
    else if (e.key === 'Enter') {
      // 브라우저 기본 Enter 동작(Chrome 계열은 새 <div>로 줄을 감싼다)에 맡기면 el의 텍스트가
      // 중첩 <div> 구조로 바뀌어, hasDirectText()가 기대하는 "직접 텍스트 자식" 조건이 깨지고
      // 이후 클릭 시 바깥 el 대신 안쪽 <div>가 선택 대상으로 잡히는 문제가 생길 수 있다.
      // execCommand('insertLineBreak')는 캐럿 위치에 <br>만 삽입하고 캐럿을 그 바로 뒤로
      // 정확히 옮겨 주므로(수동 Range 조작은 이후 타이핑이 br 앞으로 잘못 들어가는 문제가
      // 실제로 재현됐다), 평평한 구조와 명시적 줄바꿈을 모두 안정적으로 유지한다.
      e.preventDefault();
      doc.execCommand('insertLineBreak');
      if (editingInputHandler) editingInputHandler();
    }
    e.stopPropagation(); // 편집 중 Ctrl+Z 등이 우리 전역 Undo로 새지 않도록(네이티브 편집 유지)
  }

  // 편집 종료는 (1) 다른 요소를 클릭하거나(위 click 리스너의 editingTextEl 체크) (2) Escape
  // 키를 눌렀을 때만 일어난다 — 네이티브 'blur' 이벤트에 의존하지 않는다. 'blur'는 사용자가
  // 브라우저 창 자체의 포커스를 잃을 때(다른 앱으로 전환 등)도 발생하는데, 이를 "다른 곳을
  // 클릭해 편집을 끝냈다"로 오인하면 사용자가 편집 중 창만 잠깐 전환해도 편집이 조용히
  // 종료되어 버린다.
  function exitTextEditMode() {
    const el = editingTextEl;
    if (!el) return;
    el.removeEventListener('input', editingInputHandler);
    el.removeEventListener('keydown', onEditingKeydown);
    el.removeAttribute('contenteditable');
    el.classList.remove('fe-editing');
    const after = el.textContent;
    const before = editingTextBefore;
    editingTextEl = null;
    editingTextBefore = null;
    editingInputHandler = null;
    if (after !== before) {
      pushHistory([{ el, before: { textContent: before }, after: { textContent: after } }]);
      markDirty();
      setStatus('Text 내용을 수정했습니다.');
    }
  }

  // ---- Inspector 입력 반영 ----
  // 키 입력마다 1개씩 undo 항목이 쌓이지 않도록, 포커스 시점의 값을 기준으로 blur(편집 종료)
  // 시점에 한 번만 history에 기록한다. 화면/저장에 반영되는 실제 텍스트는 input마다 즉시 갱신된다.
  let textEditBefore = null;
  fContent.addEventListener('focus', () => {
    if (selected && selected.type === 'text') textEditBefore = selected.el.textContent;
  });
  fContent.addEventListener('input', () => {
    if (!selected || selected.type !== 'text') return;
    selected.el.textContent = fContent.value;
    markDirty();
  });
  fContent.addEventListener('blur', () => {
    if (!selected || selected.type !== 'text' || textEditBefore === null) return;
    const after = selected.el.textContent;
    if (after !== textEditBefore) {
      pushHistory([{ el: selected.el, before: { textContent: textEditBefore }, after: { textContent: after } }]);
    }
    textEditBefore = null;
  });

  function applyXY() {
    if (!selected) return;
    ensureAbsolute(selected.el);
    const el = selected.el;
    const slide = slideOf(el);
    const before = { left: parseFloat(el.style.left) || 0, top: parseFloat(el.style.top) || 0 };
    const w = el.offsetWidth, h = el.offsetHeight;
    // fX/fY는 항상 .slide 기준 좌표를 표시·입력받는다 — clampPosition도 .slide 기준으로
    // 판정하고, 그 결과를 writeSlidePosition으로 실제 CSS 기준(offsetParent)에 맞게 변환해
    // 쓴다. 여기서 clamped 값을 el.style.left/top에 그대로 쓰면(offsetParent가 .slide가
    // 아닐 때) 입력한 값과 렌더링 위치가 어긋난다.
    const clamped = clampPosition(parseFloat(fX.value) || 0, parseFloat(fY.value) || 0, w, h, slide.clientWidth, slide.clientHeight);
    const applied = writeSlidePosition(el, clamped.x, clamped.y);
    if (applied.left !== before.left || applied.top !== before.top) {
      pushHistory([{ el, before: { left: before.left, top: before.top }, after: { left: applied.left, top: applied.top } }]);
    }
    markDirty();
    renderHandles();
    syncInspectorFromEl(); // 경계 보정으로 값이 바뀌었을 수 있으므로 필드에 다시 반영
  }
  fX.addEventListener('change', applyXY);
  fY.addEventListener('change', applyXY);

  function applyWH() {
    // Text/Image 모두 Inspector에서 Width/Height를 직접 입력해 크기를 바꿀 수 있다.
    // Text의 경우 width를 바꾸면 font-size 등 Typography는 그대로 둔 채(el.style.width만
    // 바뀌므로) 브라우저가 그 폭에 맞춰 자동으로 줄바꿈을 다시 계산한다 — 별도 reflow 로직은
    // 필요 없다.
    if (!selected) return;
    ensureAbsolute(selected.el);
    const el = selected.el;
    const slide = slideOf(el);
    const beforeStyle = {
      width: parseFloat(el.style.width) || 1, height: parseFloat(el.style.height) || 1,
      left: parseFloat(el.style.left) || 0, top: parseFloat(el.style.top) || 0,
    };
    const beforeSlideXY = getXY(el); // 클램프는 항상 .slide 기준 현재 위치를 기준으로 판정
    const newW = Math.max(10, parseFloat(fW.value) || 1);
    const newH = Math.max(10, parseFloat(fH.value) || 1);
    const clamped = clampPosition(beforeSlideXY.x, beforeSlideXY.y, newW, newH, slide.clientWidth, slide.clientHeight);
    el.style.width = newW + 'px';
    el.style.height = newH + 'px';
    const applied = writeSlidePosition(el, clamped.x, clamped.y);
    if (newW !== beforeStyle.width || newH !== beforeStyle.height || applied.left !== beforeStyle.left || applied.top !== beforeStyle.top) {
      pushHistory([{
        el,
        before: beforeStyle,
        after: { width: newW, height: newH, left: applied.left, top: applied.top },
      }]);
    }
    markDirty();
    renderHandles();
    syncInspectorFromEl();
  }
  fW.addEventListener('change', applyWH);
  fH.addEventListener('change', applyWH);

  // ---- 드래그 이동 (단일 요소) ----
  // Pointer Capture를 요소 자신에 설정해, 드래그 중 커서가 iframe(1280x720 고정 영역) 밖으로
  // 나가도 pointermove/pointerup을 계속 이 요소가 받도록 한다. 예전에는 doc(iframe 문서)에만
  // 리스너를 달아, 커서가 iframe 밖에서 버튼을 떼면 mouseup을 영영 받지 못해 리스너가 정리되지
  // 않고 남아있다가 다음 클릭에서 엉뚱하게 반응해 "선택만 했는데 움직인다"/"드래그 후 요소가
  // 사라진다"는 두 증상을 모두 일으켰다.
  function startDrag(e) {
    ensureAbsolute(selected.el);
    const el = selected.el;
    const slide = slideOf(el);
    el.setPointerCapture(e.pointerId);
    const startX = e.clientX, startY = e.clientY;
    // history/style은 offsetParent 기준(el.style.left/top 그대로), 드래그 중 클램프 판정은
    // .slide 기준(getXY)으로 한다 — 두 좌표계를 섞으면 값이 어긋난다(위 offsetParentDelta 참조).
    const beforeStyle = { left: parseFloat(el.style.left) || 0, top: parseFloat(el.style.top) || 0 };
    const startSlide = getXY(el);
    let afterStyle = { ...beforeStyle };

    function onMove(ev) {
      const dx = ev.clientX - startX, dy = ev.clientY - startY;
      const w = el.offsetWidth, h = el.offsetHeight;
      const clamped = clampPosition(startSlide.x + dx, startSlide.y + dy, w, h, slide.clientWidth, slide.clientHeight);
      afterStyle = writeSlidePosition(el, clamped.x, clamped.y);
      syncInspectorFromEl();
      repositionHandles();
    }
    function onUp(ev) {
      el.releasePointerCapture(ev.pointerId);
      el.removeEventListener('pointermove', onMove);
      el.removeEventListener('pointerup', onUp);
      el.removeEventListener('pointercancel', onUp);
      if (afterStyle.left !== beforeStyle.left || afterStyle.top !== beforeStyle.top) {
        pushHistory([{ el, before: beforeStyle, after: afterStyle }]);
      }
      markDirty();
      renderHandles();
    }
    el.addEventListener('pointermove', onMove);
    el.addEventListener('pointerup', onUp);
    el.addEventListener('pointercancel', onUp);
  }

  // ---- 드래그 이동 (다중 선택 — 여러 요소를 같은 ΔX/ΔY로 함께 이동) ----
  // 각 요소의 개별 이동 허용 범위(슬라이드 경계 클램프)를 먼저 구한 뒤 그 교집합으로 델타를
  // 한 번만 제한하고, 그 "동일한" 델타를 전체 요소에 적용한다 — 그래야 한 요소가 먼저 경계에
  // 닿아도 요소들 사이의 상대 위치·간격이 어긋나지 않는다.
  function startGroupDrag(e, group) {
    group.forEach((item) => ensureAbsolute(item.el));
    const primaryEl = group.find((s) => s.el === e.target || s.el.contains(e.target)).el;
    primaryEl.setPointerCapture(e.pointerId);
    const startX = e.clientX, startY = e.clientY;

    const states = group.map((item) => {
      const el = item.el;
      const slide = slideOf(el);
      const beforeStyle = { left: parseFloat(el.style.left) || 0, top: parseFloat(el.style.top) || 0 };
      const startSlide = getXY(el);
      return { el, slide, beforeStyle, startSlide, w: el.offsetWidth, h: el.offsetHeight, afterStyle: { ...beforeStyle } };
    });

    let dxMin = -Infinity, dxMax = Infinity, dyMin = -Infinity, dyMax = Infinity;
    states.forEach((s) => {
      const minDx = MIN_VISIBLE_PX - s.w - s.startSlide.x;
      const maxDx = s.slide.clientWidth - MIN_VISIBLE_PX - s.startSlide.x;
      const minDy = MIN_VISIBLE_PX - s.h - s.startSlide.y;
      const maxDy = s.slide.clientHeight - MIN_VISIBLE_PX - s.startSlide.y;
      dxMin = Math.max(dxMin, Math.min(minDx, maxDx));
      dxMax = Math.min(dxMax, Math.max(minDx, maxDx));
      dyMin = Math.max(dyMin, Math.min(minDy, maxDy));
      dyMax = Math.min(dyMax, Math.max(minDy, maxDy));
    });

    function onMove(ev) {
      const rawDx = ev.clientX - startX, rawDy = ev.clientY - startY;
      const dx = Math.min(Math.max(rawDx, dxMin), dxMax);
      const dy = Math.min(Math.max(rawDy, dyMin), dyMax);
      states.forEach((s) => {
        s.afterStyle = writeSlidePosition(s.el, s.startSlide.x + dx, s.startSlide.y + dy);
      });
    }
    function onUp(ev) {
      primaryEl.releasePointerCapture(ev.pointerId);
      primaryEl.removeEventListener('pointermove', onMove);
      primaryEl.removeEventListener('pointerup', onUp);
      primaryEl.removeEventListener('pointercancel', onUp);
      const changed = states.some((s) => s.afterStyle.left !== s.beforeStyle.left || s.afterStyle.top !== s.beforeStyle.top);
      if (changed) {
        pushHistory(states.map((s) => ({ el: s.el, before: s.beforeStyle, after: s.afterStyle })));
      }
      markDirty();
    }
    primaryEl.addEventListener('pointermove', onMove);
    primaryEl.addEventListener('pointerup', onUp);
    primaryEl.addEventListener('pointercancel', onUp);
  }

  // ---- 리사이즈 핸들 (Text/Image 공통, 단일 선택일 때만) ----
  // Text는 모서리(W/H 동시 변경) 핸들에 더해 좌우 변(W만 변경) 핸들도 갖는다 — Width만 넓혀
  // 줄바꿈을 풀고 싶을 때 Height까지 함께 바뀌지 않도록 하기 위함. Image는 기존과 동일하게
  // 모서리 핸들만 유지한다(기존 동작 변경 없음).
  function removeHandles() { handleEls.forEach((h) => h.remove()); handleEls = []; }

  function computeHandlePositions(el) {
    const { x, y, w, h } = getXY(el);
    return {
      nw: [x, y], ne: [x + w, y], sw: [x, y + h], se: [x + w, y + h],
      w: [x, y + h / 2], e: [x + w, y + h / 2],
    };
  }

  function handlesForType(type) {
    return type === 'text' ? CORNERS.concat(SIDES) : CORNERS;
  }

  function renderHandles() {
    if (!selected || (selected.type !== 'image' && selected.type !== 'text') || multiSelection.length > 1) {
      removeHandles();
      return;
    }
    removeHandles();
    const slide = slideOf(selected.el);
    const positions = computeHandlePositions(selected.el);
    handlesForType(selected.type).forEach((corner) => {
      const handle = doc.createElement('div');
      handle.setAttribute('data-fe-handle', corner);
      const [px, py] = positions[corner];
      handle.style.left = (px - 5) + 'px';
      handle.style.top = (py - 5) + 'px';
      handle.style.cursor = (corner === 'w' || corner === 'e') ? 'ew-resize' : 'nwse-resize';
      handle.addEventListener('pointerdown', (e) => startResize(e, corner));
      slide.appendChild(handle);
      handleEls.push(handle);
    });
  }

  // 드래그/리사이즈가 진행 중일 때는 renderHandles()로 핸들 DOM을 통째로 재생성하면 안 된다
  // (리사이즈 핸들 자신이 Pointer Capture를 갖고 있는 도중 그 요소를 지워버리면 드래그가
  // 끊긴다). 위치만 갱신하는 가벼운 함수를 따로 둔다.
  function repositionHandles() {
    if (!selected || !handleEls.length) return;
    const positions = computeHandlePositions(selected.el);
    handleEls.forEach((handle) => {
      const corner = handle.getAttribute('data-fe-handle');
      const [px, py] = positions[corner];
      handle.style.left = (px - 5) + 'px';
      handle.style.top = (py - 5) + 'px';
    });
  }

  function startResize(e, corner) {
    e.stopPropagation();
    e.preventDefault();
    ensureAbsolute(selected.el);
    const el = selected.el;
    const slide = slideOf(el);
    const handle = e.currentTarget;
    handle.setPointerCapture(e.pointerId);
    // start: .slide 기준(getXY) — 드래그 중 클램프 판정 기준점.
    // beforeStyle: offsetParent 기준(el.style.*) — history/undo에 그대로 쓸 수 있는 실제 값.
    const start = getXY(el);
    const beforeStyle = {
      left: parseFloat(el.style.left) || 0, top: parseFloat(el.style.top) || 0,
      width: parseFloat(el.style.width) || start.w, height: parseFloat(el.style.height) || start.h,
    };
    const startX = e.clientX, startY = e.clientY;
    let afterStyle = { ...beforeStyle };

    function onMove(ev) {
      const dx = ev.clientX - startX, dy = ev.clientY - startY;
      let { x, y, w, h } = start;
      if (corner.includes('e')) w = Math.max(10, start.w + dx);
      if (corner.includes('s')) h = Math.max(10, start.h + dy);
      if (corner.includes('w')) { w = Math.max(10, start.w - dx); x = start.x + dx; }
      if (corner.includes('n')) { h = Math.max(10, start.h - dy); y = start.y + dy; }
      const clamped = clampPosition(x, y, w, h, slide.clientWidth, slide.clientHeight);
      const applied = writeSlidePosition(el, clamped.x, clamped.y);
      el.style.width = w + 'px';
      el.style.height = h + 'px';
      afterStyle = { left: applied.left, top: applied.top, width: w, height: h };
      syncInspectorFromEl();
      repositionHandles();
    }
    function onUp(ev) {
      handle.releasePointerCapture(ev.pointerId);
      handle.removeEventListener('pointermove', onMove);
      handle.removeEventListener('pointerup', onUp);
      handle.removeEventListener('pointercancel', onUp);
      if (afterStyle.left !== beforeStyle.left || afterStyle.top !== beforeStyle.top ||
          afterStyle.width !== beforeStyle.width || afterStyle.height !== beforeStyle.height) {
        pushHistory([{ el, before: beforeStyle, after: afterStyle }]);
      }
      markDirty();
      renderHandles();
    }
    handle.addEventListener('pointermove', onMove);
    handle.addEventListener('pointerup', onUp);
    handle.addEventListener('pointercancel', onUp);
  }

  // ---- 이미지 교체 ----
  fImageFile.addEventListener('change', async () => {
    if (!selected || selected.type !== 'image' || !fImageFile.files[0]) return;
    const file = fImageFile.files[0];
    const dataUrl = await new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onload = () => resolve(reader.result);
      reader.onerror = reject;
      reader.readAsDataURL(file);
    });
    setStatus('이미지 업로드 중...');
    try {
      const res = await fetch('/api/upload-image', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ filename: file.name, dataUrl }),
      });
      const data = await res.json();
      if (!data.ok) { setStatus('이미지 업로드 실패: ' + (data.error || ''), true); return; }
      const beforeSrc = selected.el.getAttribute('src');
      selected.el.setAttribute('src', data.path);
      pushHistory([{ el: selected.el, before: { src: beforeSrc }, after: { src: data.path } }]);
      markDirty();
      setStatus('이미지가 교체되었습니다. 저장을 눌러 반영하세요.');
    } catch (err) {
      setStatus('이미지 업로드 오류: ' + err, true);
    }
    fImageFile.value = '';
  });

  // ---- 저장 (에디터 전용 표시 요소 제거 후 직렬화) ----
  function serializeCleanHTML() {
    if (editingTextEl) exitTextEditMode(); // 편집 중이던 내용을 커밋하고 contenteditable 속성 제거

    const styleEl = doc.getElementById('fe-style');
    if (styleEl) styleEl.remove();
    removeHandles();
    const selEl = selected ? selected.el : null;
    if (selEl) selEl.classList.remove('fe-selected');
    multiSelection.forEach((s) => s.el.classList.remove('fe-selected'));
    // 방어적 정리: 어떤 경로로든 contenteditable이 남아있는 요소가 있다면 저장 전에 제거한다.
    doc.querySelectorAll('[contenteditable]').forEach((el) => el.removeAttribute('contenteditable'));

    // reflow 방지용 placeholder(ensureAbsolute 참조)는 저장되는 HTML에는 남기지 않는다.
    // 단, 직렬화가 끝나면 즉시 같은 자리에 되돌려 놓아야 한다 — 그 사이라도 DOM에서 없어지면
    // 편집을 계속하는 동안 sibling이 다시 reflow될 수 있다.
    const placeholders = Array.from(doc.querySelectorAll('[data-fe-placeholder]'));
    const placeholderAnchors = placeholders.map((p) => ({ p, parent: p.parentNode, next: p.nextSibling }));
    placeholders.forEach((p) => p.remove());

    const html = '<!DOCTYPE html>\n' + doc.documentElement.outerHTML;

    placeholderAnchors.forEach(({ p, parent, next }) => parent.insertBefore(p, next));
    if (styleEl) doc.head.appendChild(styleEl);
    if (selEl) selEl.classList.add('fe-selected');
    multiSelection.forEach((s) => s.el.classList.add('fe-selected'));
    if (selected && selected.type === 'image' && multiSelection.length <= 1) renderHandles();
    return html;
  }

  saveBtn.addEventListener('click', async () => {
    setStatus('저장 중...');
    try {
      const html = serializeCleanHTML();
      const res = await fetch('/api/save', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ html }),
      });
      const data = await res.json();
      if (data.ok) {
        dirty = false;
        setStatus('저장 완료: ' + data.path);
      } else {
        setStatus('저장 실패: ' + (data.error || ''), true);
      }
    } catch (err) {
      setStatus('저장 오류: ' + err, true);
    }
  });

  function showResultBanner(sharedPath, qaText) {
    resultBanner.hidden = false;
    resultPath.textContent = sharedPath;
    resultQa.textContent = qaText || '';
  }

  bundleBtn.addEventListener('click', async () => {
    setStatus('공유용 HTML(shared.html) 생성 중...');
    try {
      const res = await fetch('/api/bundle', { method: 'POST' });
      const data = await res.json();
      if (data.ok && data.shared_html_path) {
        showResultBanner(data.shared_html_path, '(구조 QA는 실행하지 않았습니다 — "최종 확정" 버튼을 쓰면 QA까지 함께 수행됩니다.)');
      }
      setStatus(
        data.ok ? 'shared.html 생성 완료' : ('번들 실패: ' + (data.stderr || '').slice(0, 200)),
        !data.ok,
      );
    } catch (err) {
      setStatus('번들 요청 오류: ' + err, true);
    }
  });

  finalizeBtn.addEventListener('click', async () => {
    setStatus('최종 확정 처리 중... (저장 → 전체 슬라이드 구조 QA → 공유용 HTML 생성)');
    finalizeBtn.disabled = true;
    try {
      const html = serializeCleanHTML();
      const res = await fetch('/api/finalize', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ html }),
      });
      const data = await res.json();
      if (data.ok && data.shared_html_path) {
        dirty = false;
        const flagged = data.flagged_slides || [];
        const qaText = flagged.length
          ? `구조 QA 경고: ${flagged.length}개 슬라이드에서 겹침/캔버스 이탈/잘림이 발견됐습니다 (${flagged.join(', ')}). 필요하면 계속 수정한 뒤 다시 "최종 확정"을 누르세요.`
          : '구조 QA: 전체 슬라이드에서 겹침/캔버스 이탈/잘림 없음 (clean)';
        showResultBanner(data.shared_html_path, qaText);
        setStatus('최종 확정 완료');
      } else {
        setStatus('최종 확정 실패: ' + (data.bundle_stderr || data.qa_stderr || data.error || '알 수 없는 오류').slice(0, 200), true);
      }
    } catch (err) {
      setStatus('최종 확정 오류: ' + err, true);
    } finally {
      finalizeBtn.disabled = false;
    }
  });

  qaBtn.addEventListener('click', async () => {
    setStatus('구조 QA 재검증 중... (겹침/overflow/clipping)');
    try {
      const res = await fetch('/api/qa', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ slides: String(currentIndex + 1) }),
      });
      const data = await res.json();
      qaPanel.hidden = false;
      if (!data.ok && !data.layout_audit) {
        qaOutput.textContent = 'QA 실행 실패:\n' + (data.stderr || data.error || '알 수 없는 오류') +
          '\n\n(playwright가 설치되어 있어야 합니다: pip install playwright && playwright install chromium)';
        setStatus('구조 QA 실행 실패', true);
        return;
      }
      const audit = data.layout_audit || {};
      const key = `slide_${currentIndex + 1}`;
      const result = audit[key];
      if (!result) {
        qaOutput.textContent = '이 슬라이드에 대한 QA 결과를 찾을 수 없습니다.';
      } else if (!result.flagged) {
        qaOutput.textContent = `슬라이드 ${currentIndex + 1}: 겹침/이탈/잘림 없음 (clean)`;
      } else {
        qaOutput.textContent =
          `슬라이드 ${currentIndex + 1}: 문제 발견\n` +
          `- overflow(캔버스 이탈): ${result.overflow.length}건\n` +
          `- clipped(잘림): ${result.clipped.length}건\n` +
          `- overlaps(겹침): ${result.overlaps.length}건\n\n` +
          JSON.stringify(result, null, 2);
      }
      setStatus('구조 QA 재검증 완료');
    } catch (err) {
      setStatus('QA 요청 오류: ' + err, true);
    }
  });
})();
