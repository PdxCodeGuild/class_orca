Vue.component("student-list", {
    template: `
    <div id="students">
        <div v-for="student in students" :key="student.id">
            <p> {{ student.last_name}} </p>
        </div>
    </div>
    `,
    props: ["students"],
})
Vue.component("add-new-student", {
    template: `
    <div>
        <div id="add-student" v-for="field in newStudent" :key="field.id" i=0>
            <input v-model=newStudent.field placeholder=form_fields[i] i++>
        </div>
        <button type="submit" @click="addStudent">Submit</button> 
    </div>
    `,
    props: ['newStudent', 'show'],
    data: function () {
        return {
            form_fields: ['First Name', 'Last Name', 'Cohort', 'Favorite Topic', 'Capstone']
        }
    },
    methods: {
        addStudent: function () {
            axios({ 
                method: "post",
                url: "/api/v1/",
                headers: {
                    'X-CSRFToken': this.csrf_token
                },
                data: this.newStudent
            }).then(response => {
                this.loadStudentList()
                this.newStudent = {
                    "first_name": "",
                    "last_name": "",
                    "cohort": "",
                    "favorite_topic": "",
                    "favorite_teacher": "",
                    "capstone": "",
                }
            }).catch(error => {
                console.log(error.response.data)
            })
        }    
    }
})
let vm = new Vue ({
    el: "#app",
    data: {
        students: {},
        newStudent: {
            "first_name": "",
            "last_name": "",
            "cohort": "",
            "favorite_topic": "",
            "favorite_teacher": "",
            "capstone": "",
        },
        csrf_token: "",
    },
    methods: {
        loadStudentList: function () {
            axios({
                method: "get",
                url: "/api/v1/",
            }).then(response => {
                this.students = response.data
                console.log(this.students)
            })
        },
    },
    created: function () {
        this.loadStudentList() 
    },
    mounted: function() {
        this.csrf_token = document.querySelector('input[name="csrfmiddlewaretoken"]').value
    }
})