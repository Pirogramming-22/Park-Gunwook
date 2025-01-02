let timer;
let elapsedMilliseconds = 0;
const display = document.getElementById('time-display');
const startButton = document.getElementById('start-button');
const stopButton = document.getElementById('stop-button');
const resetButton = document.getElementById('reset-button');
const lapList = document.getElementById('lap-list');
const clearLaps = document.getElementById('clear-laps');
const selectAllButton = document.getElementById('select-all-laps');

// 디스플레이 업데이트 함수
function updateDisplay() {
    const seconds = Math.floor(elapsedMilliseconds / 1000); // 초 단위
    const milliseconds = Math.floor((elapsedMilliseconds % 1000) / 10); // 밀리초 단위 (10ms 단위)
    display.textContent = `${String(seconds).padStart(2, '0')}:${String(milliseconds).padStart(2, '0')}`;
}

// 타이머 시작 함수
function startTimer() {
    if (!timer) {
        const startTime = Date.now() - elapsedMilliseconds;
        timer = setInterval(() => {
            elapsedMilliseconds = Date.now() - startTime;
            updateDisplay(); // 타이머가 갱신될 때마다 디스플레이 업데이트
        }, 10);
    }
}

// 타이머 중지 함수
function stopTimer() {
    clearInterval(timer); // 타이머 멈추기
    timer = null;
    addLap(); // 중지 시 자동으로 구간 기록 추가
}

// 타이머 리셋 함수
function resetTimer() {
    clearInterval(timer); // 타이머 클리어
    timer = null; // 타이머 상태 초기화
    elapsedMilliseconds = 0; // 경과 시간 초기화
    updateDisplay(); // "00:00"으로 디스플레이 초기화
}

// 구간 기록 추가 함수
function addLap() {
    const lapItem = document.createElement('li'); // 새로운 구간 항목 생성

    const checkBox = document.createElement('input'); // 체크박스 생성
    checkBox.type = 'checkbox';
    checkBox.style.marginRight = '10px';
    checkBox.style.borderRadius = '50%';

    const lapText = document.createElement('span'); // 구간 시간 텍스트 생성
    lapText.textContent = display.textContent;

    lapItem.appendChild(checkBox); // 체크박스 추가
    lapItem.appendChild(lapText); // 구간 시간 추가
    lapList.appendChild(lapItem); // 구간 목록에 추가

    checkBox.addEventListener('change', updateSelectAllButton);
    updateSelectAllButton();
}

// 선택된 구간 기록 삭제 함수
function clearLapRecords() {
    const checkedItems = Array.from(lapList.querySelectorAll('input[type="checkbox"]:checked'));
    checkedItems.forEach((item) => {
        const lapItem = item.parentElement; // 체크된 항목의 부모 요소(구간 항목) 제거
        lapList.removeChild(lapItem);
    });

    selectAllButton.checked = false;
}

// 모든 구간 기록 선택 함수
function selectAllLaps() {
    const allCheckBoxes = lapList.querySelectorAll('input[type="checkbox"]');
    const allChecked = Array.from(allCheckBoxes).every(checkBox => checkBox.checked);

    allCheckBoxes.forEach((checkBox) => {
        checkBox.checked = !allChecked; // 모든 체크박스를 반대로 설정 (선택된 상태라면 해제, 아니면 선택)
    });

    updateSelectAllButton();
}

function updateSelectAllButton() {
    const allCheckBoxes = lapList.querySelectorAll('input[type="checkbox"]');
    const allChecked = Array.from(allCheckBoxes).every(checkBox => checkBox.checked);

    selectAllButton.checked = allChecked; // 모든 체크박스가 선택되었으면 "Select All" 버튼도 선택됨
}

// 이벤트 리스너 추가
startButton.addEventListener('click', startTimer); // 시작 버튼 클릭 시 타이머 시작
stopButton.addEventListener('click', stopTimer); // 정지 버튼 클릭 시 타이머 중지
resetButton.addEventListener('click', resetTimer); // 리셋 버튼 클릭 시 타이머 초기화
clearLaps.addEventListener('click', clearLapRecords); // 구간 기록 삭제 버튼 클릭 시 기록 삭제
selectAllButton.addEventListener('click', selectAllLaps); // "Select All" 버튼 클릭 시 모든 구간 선택

updateDisplay(); // 페이지 로딩 시 초기 디스플레이 업데이트