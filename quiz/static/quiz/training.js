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
            this.answerIsVisible = false;

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
            userAnswer = this.userAnswer.replace(/\s+/g, ' ').trim();
            answer = this.answer.replace(/\s+/g, ' ').trim();

            if (userAnswer == answer) {
                this.getQuestion();
            }
        },

        skipQuestion() {
            this.getQuestion();
        }
    }
});