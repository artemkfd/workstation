'use strict';

window.addEventListener('DOMContentLoaded', () => {
    console.log('loaded search');
    const div = document.querySelector('.search_result');

    const request = new XMLHttpRequest();

    request.open('GET', 'search');

    request.addEventListener('load', () =>{
        console.log('load get произошло');
        if (request.status === 200) {
            console.log(request.response)
            console.log('200 get получили');
        } else {
            console.log('200 get не получили');
        }

    });
    let result = {{ results }};
    console.log(result);






});