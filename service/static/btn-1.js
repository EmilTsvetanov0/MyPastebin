document.querySelectorAll('.btn1').forEach(function(button) {
    button.addEventListener('click', function() {
        this.classList.add('on-click-animation');

        // Удаляем класс после завершения анимации
        setTimeout(() => {
            this.classList.remove('on-click-animation');
        }, 300); // Длительность анимации 0.3 секунды
    });
});
