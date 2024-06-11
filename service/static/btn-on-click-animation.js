document.querySelectorAll('.btn-1').forEach(function(button) {
    button.addEventListener('click', function() {
        this.classList.add('shadow-animation');

        // Удаляем класс после завершения анимации
        setTimeout(() => {
            this.classList.remove('shadow-animation');
        }, 2000); // Длительность анимации 2 секунды
    });
});
