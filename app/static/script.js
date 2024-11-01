// 파일 업로드 시 미리보기 기능
document.addEventListener('DOMContentLoaded', function () {
    const fileInput = document.querySelector('input[type="file"]');
    const form = document.querySelector('form');

    if (fileInput && form) {
        fileInput.addEventListener('change', function () {
            if (fileInput.files.length > 0) {
                alert('파일이 선택되었습니다: ' + fileInput.files[0].name);
            }
        });

        // 업로드 버튼 클릭 시 알림 메시지 표시
        form.addEventListener('submit', function (event) {
            alert('영수증이 업로드됩니다. 잠시만 기다려주세요.');
        });
    }
});
