let vm = new Vue({
    el:'#app',

    data:{
        chordname:'',
        chordroot:'',
        strings:'',
        fingering:'',
        flatorsharp:'',
        majororminor:'',
        seventh:'',
        showpic: false,
        diagramtoshow:'',
        diagram:{
            'A':'images/A.png',
            'A7':'images/A7.png',
            'Ab':'images/Ab.png',
            'Am':'images/Am.png',
            'B':'images/B.png',
            'Bm':'images/Bm.png',
            'B7':'images/B7.png',
            'Bb':'images/Bb.png',
            'Bb7':'images/Bb7.png',
            'Bbm':'images/Bbm.png',
            'C':'images/C.png',
            'Cm':'images/Cm.png',
            'C7':'images/C7.png',
            'C#m':'images/C#m.png',
            'C#':'images/Db.png',
            'D':'images/D.png',
            'Dm':'images/Dm.png',
            'D7':'images/D7.png',
            'Db':'images/Db.png',
            'Eb':'images/E flat.png',
            'Eb7':'images/Eb7.png',
            'E':'images/E.png',
            'E7':'images/E7.png',
            'Em':'images/Em.png',
            'F':'images/F.png',
            'Fm':'images/Fm.png',
            'F7':'images/F7.png',
            'F#':'images/F#.png',
            'F#7':'images/F#7.png',
            'F#m':'images/F#m.png',
            'G':'images/G.png',
            'G7':'images/G7.png',
            'Gm':'images/Gm.png',
            'G#m':'images/Gm.png'

        }
        
        },
        computed:{
            chordnamesend: function(){
                chord = `${this.chordroot}${this.flatorsharp}${this.majororminor}${this.seventh}`
                this.chordname=chord.trim()
                return `${this.chordroot}${this.flatorsharp}_${this.majororminor}${this.seventh}`
            },
            // showdiagram: function(){
               
            //     if(this.diagram[this.chordname]){
            //         console.log('it worked')
            //         this.showpic = true
            //     } else {
            //       this.showpic= false 
            //     }
            // }
            
        },
        methods: {
            loadChord: function(evt){
                        
                        console.log(this.chordname)
                        axios({
                        url: `https://api.uberchord.com/v1/chords/${this.chordnamesend}`,
        
                        method: "get",
        
                        headers:{
                        //   "Authorization": `Token token="a51b4c035f2554ba87f3e30c52f9105e"`
                        },
                        params: {
                                // filter: this.searchTerm,
                                // type: this.searchby,
                                // page:this.pages
        
                        }
                  }).then(response =>{
                    //   this.chordname= response.data.chordname
                    //   this.chordname = this.chordroot
                      this.fingering = response.data[0].fingering
                      this.strings = response.data[0].strings
                      console.log(this.chordname)
                      console.log(response.data)
                      if(this.diagram[this.chordname]){
                        console.log('it worked', this.diagram[this.chordname])
                        this.showpic = true
                        this.diagramtoshow = this.diagram[this.chordname]
                    } else {
                      this.showpic= false 
                    }
                  }) 
                },
                searchReset:function(){
                    this.chordroot = ''
                    this.majororminor = ''
                    this.flatorsharp = ''
                    this.seventh = ''
                    this.fingering=''
                }
        // created(){ 
        //     this.pageLoadquotes()
        // }

      }
    
    })
    