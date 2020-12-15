//v2, with a component

/* <input v-if="editing" type="text" v-model="task.newTaskText" @keyup.enter="editTask">\ */
// 
// 

Vue.component('task', {
  template: `
    <li>
      <button v-on:click="$emit('swap', task)">✓</button>
      {{ task.task_name }}
      <button v-on:click="$emit('remove', task)">(!) Delete</button>
    </li>
  `,
  props: ['task'],
})


new Vue({
  el: '#to-do-list',
  data: { 
    message: 'Hello00000 Vue!',     //     ;)
    newTaskText: '',
    task_list: [
      {id: 0,
        task_name: 'Understand VUE...',
        completed: false,
      },
      {id: 101,
        task_name: 'i somewhat like my new dew: vue',
        completed: true,
      },
      {id: 102,
        task_name: 'i want to see the lights at the zoo',
        completed: true,
      },
      {id: 103,
        task_name: 'frameworks are hard, though fast they can be',
        completed: true,
      },
      {id: 104,
      task_name: 'there\'s lots going on that i cannot see\\',
      completed: true,
      },
      // are semicolons there, or bare?
      // should i put this syntax anywhere?
      // my mentors say, "stick with it, loosen your brow!"
      // "you'll get there someday", i say: 'how now, brown cow?'
      // 
      // 
    ],
    nextTaskID: 2
  },
  methods: {
    addNewTask: function() {
      console.log(event),
      console.log(`performing function addNewTask, this.newTaskText: ${this.newTaskText}`),
      this.task_list.push({
        id: this.nextTaskID++,
        task_name: this.newTaskText,
        completed: false,
      })
      this.newTaskText = ''
    }, // and i needed this comma!
    swap_completed: function(index) {
      console.log('attempting function swap_completed(index)'),
      console.log(event),
      console.log(`for index: ${index}`),
      console.log(`for index.task_name: ${index.task_name}`),
      console.log(this.task_list[index].completed)
      if (this.task_list[index].completed === true) {
        this.task_list[index].completed = false
      }
      else if (this.task_list[index].completed === false) {
        this.task_list[index].completed = true
      }
    },
    delete_task: function(index) {
      console.log(`delete_task for index: ${index}`);
      console.log(event);
      this.task_list.splice(index, 1);
    },
  }
});

//not using this anymore:

// NOTES: 

// from monday 14 dec:
// v-show is better if it's *frequently* shown and hidden, so it'll stay in memory
// but v-if is a bit more intensive...
// pay [?]
// template tag in a component is JUST FOR US

// C:\-=Cloud=-\Sync\git_working\week9_javascript\lab11_to_do_list_in_JS-VUE

// TODO read about components: 
// https://vuejs.org/v2/guide/components.html

// <!-- NEED TO USE A KEY, otherwise stuff gets wierd when checking boxes... -->

// <!-- BEFORE using watched property, use computed property and methods instead... -->

// // NOTES FROM MERRIT'S REVIEW OF THIS ON THURS, 10 DEC 2020:

// function addTodoCallback() {
//     const todoText = 
//     // remove button:
//         // remove parent element
//     // TO-DO LOOKUP JAVASCRIPT 'this'
// };
// // END THOSE NOTES

// Your Vue app will need to do a few things:
// Store an array of objects (the todos themselves)
// List each todo
// Allow the user to add and remove todos
// Allow a user to toggle if a task is complete or not