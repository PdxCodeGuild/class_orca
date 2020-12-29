<!--
    Comments:
    
    https://docs.github.com/en/free-pro-team@latest/github/writing-on-github/basic-writing-and-formatting-syntax 
    
    https://github.com/PdxCodeGuild/class_orca/blob/main/5%20Capstone/Capstone%20Proposal.md
    
    https://github.com/PdxCodeGuild/class_orca/blob/main/4%20JavaScript/labs/lab08-bouncing_ball.md 
 
 -->

<!--  -->

<!--  -->
# Childhood Canvas, o 'Tela di infanzia'
   - ### by John Fial
   - ### PDX Code Guild, Class Orca, Oct 2020 – Jan 2021
   - ### Capstone Proposal, 28/29 December, 2020

<!--  -->
# Project Overview

- Childhood Canvas is a visual play sandbox for older babies and toddlers, intended for full-screen (lock screen), very limited-feature use.

<!--  -->
### Project Philosophy:
   -  Apart from most existing programs, it is meant to **stimulate two-handed interaction** with the digital keyboard, as opposed to the analog mouse. 
   - **User audience**: the aim here is older babies and toddlers < 3, not older children who might want to draw more complex art. 
   - The project should also make it obvious to parents/adult caretakers just how much neurological 'masturbation' -- if I may use that term -- is involved in the human-computer's iconic input > output cycle. Video games, of couse, are the ultimate epitome of this cycle. (And although today's systems are somewhat beginning to implement a 3D/gravitational/Z-axis/VR aspect, we are a long way from either A) directly connecting to the brain, or B) adding other sensory informaiton, such as smells/tastes, temperature/skin pressure etc., ... but I digress! )
   - Indeed, **the goal is for the canvas to be anti-addictive**. That is, in contrast with the infinite capabilities of computers, the young user should exhaust interest in the canvas' capabilities within 20-45 minutes. After a week of such daily sessions, the canvas should allow new features (my job) as the child grows.

<!--  -->
# Features / User Stories


0. User Story **Example:** "As a _____ (user), I want _____ (feature) because _____ (reason)."
   - Tasks: 
      - [ ] a
      - [ ] b
      - [ ] c

1. - As a parental/caregiver accountholder, I want the ability to have multiple profiles (for different children/adults) under my one account so that everything's in one place.
   - Tasks: 
      - [ ] Create Custom User Model WITH different users/children within that...
      - [ ] Create several Test Logins


0. User Story **Example:** "As a _____ (user), I want _____ (feature) because _____ (reason)."
   - Tasks: 
      - [ ] a
      - [ ] b
      - [ ] c

10. As a child, I want **music** because silent computer time is boring!
   - Tasks: 
      - [ ] a
      - [ ] b
      - [ ] c

99. As a user, I want to be able to **save or print my/our drawings**, and would love these to save to the account (in the cloud, accessible from anywhere).
   - Tasks: 
      - [ ] a
      - [ ] b
      - [ ] c

999. As a user, I want to be comfortable using the app at night or day, so I need a light/dark mode.
   - Tasks: 
      - [ ] Add dark mode
      - [ ] Check system default, put current mode into system default
      - [ ] Add ability for user to permanently select in their account (or user profile?!) settings

<!--  -->
# Data Model (minimal django)

   - Account
      - User 1 : Name
      - ***Question:*** Does this kind of functionality need a custom user model?

   *Because so much of this project should be within canvas, I don't think I need much in the way of django models, right? Whereas the music project (see the other .md) would have a lot more here...*

<!--  -->
# Schedule

***Question:*** Which of these dates are too agressive, or not agressive enough?

   - January Calendar: 
      - -M / -W / -F
      - 04 / 06 / 08
      - 11 / 13 / 15
      - 18 / 20 / -- / (18 is MLK, Jr. Day, 21st is Presentations )


## MVP 0/10, 31 Dec, Wednesday **MORNING**, Project Creation, Custom User Model, Sign in and Welcome page
   - Custom User Login/Accounts, see https://learndjango.com/tutorials/django-custom-user-model

---

## MVP 1/10, 05 Jan, Tuesday, Custom User Model, Working Fullscreen Lock, Django/Vue
   - Ideally, the screen is locked -- i.e.: even though the child has inevitably seen more complex information on the screen, they cannot exit to the OS, and must remain within the blank canvas. (This may or may not be allowable based on the OS, browser, JS/HTML5 permissions, or addons.) Depending on complexity, keypresses might a) do nothing, or b) change the most basic output.

## MVP 2/10, 08 Jan, Friday, Basic Keyboard functionality
   - each keypress interacts with screen:
      - v1: Keypress adds that character to screen at random position, set font size
      - v2: Keypress 

---

## MVP 3/10, 13 Jan, Wednesday DEPLOY TO WEB, via pythonAnywhere / etc.
   - This is important because I don't want to procrastinate until after class... but then never do it
   - Link to this deployed project from my portfolio page

---

## MVP 4/10, 18 Jan, Monday Standard Draw Functionality:
   - Keypress output: set font size, cursor, random or set position, reset/lock invisible cursor position
   - Set keypress to draw different shapes, animal icons, etc.
   - Mouse : draw ability, different paintbrushes (thickness, color, line/brush/dashed/etc.)

## MVP 5/10, 20 Jan, Wednesday Add optional background Music + Volume bar 
   - (default off, prefer keyboard on/off)

---

## MVP 6/10, Future: Change user age (app mode)
   - This is to switch between simpler versions of the app, for, say, babies (button press makes a shape appear) versus, say, an older toddler version, where they might select a truck, human, or tree and then click to get those on the screen. 
   - Or it might let the user (or adult) switch between functionality; between, say: 
      - A, which makes keypresses add that letter to a random position on the screen with a random color, and 
      - B, which makes keypresses 'draw' different figures in the same spot, slowly drawing a pre-defined (but invisible) piece of art
      - C, which makes keypresses draw letters sequentially (normal typing), and 
   - etc...

## MVP 7/10, Future: Save/Print Art
   - Depending on image size, allow saving to the website or sharing as a temporary link.

## MVP 9/10 : Future: 
## MVP 10/10 : Future: 

## Other ideas:
   - Light/Dark mode (add to my portfolio, too!)
   - 



<!--  -->

---

.
---
.
---
.
---
.
---
.
---
.
---
.
---
.
---
.

---


<!--  -->
# Notes for formatting .md files:

\# The largest heading (includes \<hr>):
# The largest heading


\## The second largest heading:
## The second largest heading

\###### The smallest heading:
###### The smallest heading

---

**This is bold text**

*This text is italicized*	

~~This was mistaken text~~

**This text is _extremely_ important**

***All this text is important***

---
Quoted text is 
> like this

---

Lists

You can make an unordered list by preceding one or more lines of text with - or *.

1. First list item
   - First nested list item
     - Second nested list item

---

1. James Madison
2. James Monroe
3. John Quincy Adams

---

## Checklists:

- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request

---

If a task list item description begins with a parenthesis, you'll need to escape it with \\