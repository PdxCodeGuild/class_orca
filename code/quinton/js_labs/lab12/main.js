const app = new Vue ({
    el: '.calculator',
    data() {
        return {
            firstNum: null,
            current: '',
            operator: null,
            operatorClicked: false
        }
    },
    methods: {
        clear() {
            this.current = '';
        },
        append(number) {
            if (this.operatorClicked) {
                this.current = '';
                this.operatorClicked = false;
            }
            this.current = `${this.current}${number}`;
        },
        dot() {
            if (this.current.indexOf('.') === -1) {
                this.append('.');
            }
        },
        setFirstNum() {
            this.firstNum = this.current;
            this.operatorClicked = true;
        },
        divide() {
            this.operator = (a, b) => a / b;
            this.setFirstNum();
        },
        multiply() {
            this.operator = (a, b) => a * b;
            this.setFirstNum();
        },
        add() {
            this.operator = (a, b) => a + b;
            this.setFirstNum();
        },
        subtract() {
            this.operator = (a, b) => a - b;
            this.setFirstNum();
        },
        equals() {
            this.current = `${this.operator(parseFloat(this.firstNum), parseFloat(this.current))}`;
            this.previous = null;
        }
    }
})