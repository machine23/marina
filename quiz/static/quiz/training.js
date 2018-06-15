// window.onload = getQuestion;
// let form = document.querySelector('#quiz_form');
// let skip_btn = document.querySelector('#skip');
// skip_btn.onclick = getQuestion;
// let answer = '';
// form.onsubmit = checkAnswer;
// function getQuestion(e) {
//     fetch(URL, {
//         credentials: 'include',
//     })
//         .then(response => response.json())
//         .then(json => {
//             console.log(json)
//             document.querySelector('#question').innerHTML = json.question;
//             document.querySelector('#answer').value = '';
//             document.querySelector('#id_answer').value = '';
//             answer = json.answer.trim().replace('\r\n', '\n');
//         })
// }
// function checkAnswer(e) {
//     e.preventDefault();
//     user_answer = document.querySelector('#id_answer').value;
//     if (user_answer == answer) {
//         getQuestion();
//     } else {
//         document.querySelector('#answer').value = answer;
//     }
// }

new Vue({
    el: '#training-app',
    delimiters: ['${', '}'],
    data: {
        question: '',
        answer: 'answer',
        userAnswer: '',
        answerIsVisible: false,
    },
    mounted: function () {
        this.getQuestion();
    },
    methods: {
        toggleAnswerVisible() {
            this.answerIsVisible = !this.answerIsVisible;
        },

        getQuestion() {
            this.userAnswer = '';

            fetch(URL, {
                    credentials: 'include',
                })
                .then(response => response.json())
                .then(json => {
                    console.log(json);
                    this.question = json.question;
                    this.answer = json.answer.trim().replace('\r\n', '\n');
                }
            )
        },

        checkAnswer() {
            console.log(this.userAnswer);
            console.log((this.userAnswer == this.answer))
            if (this.userAnswer.trim() == this.answer) {
                this.getQuestion();
            }
        },

        skipQuestion() {
            this.getQuestion();
        }
    }
});