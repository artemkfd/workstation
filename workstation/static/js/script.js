'use strict';

window.addEventListener('DOMContentLoaded', () => {
    console.log('loaded');
    const btnLess = document.querySelector('#option1');
    const btnMore = document.querySelector('#option2');
    btnMore.innerHTML = "hello";
    const textarea = document.querySelector('textarea');

    $(function () {
      $('[data-toggle="tooltip"]').tooltip()
    })
    btnLess.title = "Добавить аннулированные машины вручную, либо вставить в поле ввода, либо добавить файл с аннулированными машинами";
    btnMore.title = "Проверить весь реестр на состояние пропуска";
    function toggleBtn() {
        console.log('hi');
    }

    textarea.addEventListener('move', console.log('hell0000o'));
    textarea.addEventListener('input', function(eve) {
        eve.preventDefault();
        console.log(eve.target);
        console.log(eve.target.value);

    });


});