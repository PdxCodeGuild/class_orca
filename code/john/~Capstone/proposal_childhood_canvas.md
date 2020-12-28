<!-- https://docs.github.com/en/free-pro-team@latest/github/writing-on-github/basic-writing-and-formatting-syntax -->
<!-- 
    Comments:
    https://github.com/PdxCodeGuild/class_orca/blob/main/5%20Capstone/Capstone%20Proposal.md
    
    Music https://github.com/PdxCodeGuild/class_orca/blob/main/4%20JavaScript/labs/lab08-bouncing_ball.md 
 -->



John Fial
PDX Code Guild, Class Orca, Oct 2020 – Jan 2021
Capstone Proposal, 28/29 December, 2020

# Childhood Canvas

---

# Project Overview

- Childhood Canvas is meant to be a full-screen/(screen-lock) limited-feature visual input/output play sandbox for older babies and toddlers.

## Project Philosophy:
   -  Apart from most existing programs, it is meant to stimulate two-handed interaction with the digital keyboard, as opposed to the analog mouse. 
   - User audience: the aim here is older babies and toddlers < 3, not older children who might want to draw more complex art. 
   - The project should also make it obvious to parents/adult caretakers just how much neurological 'masturbation' -- if I may use that term -- is involved on the computer's iconic input > output cycle. Video games, of couse, are the ultimate epitome of this cycle. And although today's systems are somewhat beginning to implement a 3D/gravitational/Z-axis 


# Features / User Stories

- As a parental accountholder, I want the ability to have multiple profiles (for different children/adults) under my one account so that everything's in one place.

Then, any key/button pressed should provide a visual output. 



# Data Model (minimal django)

- What data will you need to store as part of your application? These should be specific nouns, collections of information that serve a collective purpose. Examples might be 'User', 'Book', 'ImageSet'. These are schemas for your data models (database tables).

## User Profiles:
   - User
   - aoeu




# Schedule
   (This should serve as both a blueprint and a to-do list of everything to do...)

## MVP 1 / * : Working Fullscreen Lock, Django/Vue/
   
   -Ideally, the screen is locked -- i.e.: even though the child has inevitably seen more complex information on the screen, they cannot exit to the OS, and must remain within the blank canvas.

## MVP 3 / * : Basic Keyboard functionality

   - each keypress interacts with screen
      - v1: Keypress adds that character to screen at random position, set font size
      - v2: Key 

## MVP 5 / * : Working User Login/Accounts

## MVP 6 / * : DEPLOY TO WEB, via pythonAnywhere / etc.
   - This is important because I don't want to procrastinate until after class... but then never do it
   - Link to this deployed project from my portfolio page

## MVP 6 / * : Standard Draw Functionality:
   - Keypress output: set font size, cursor, random or set position, reset/lock invisible cursor position
   - Set keypress to draw different shapes, animal icons, etc.
   - Mouse : draw ability, different paintbrushes (thickness, color, line/brush/dashed/etc.)


## MVP 6 / * : Save/Print Art
   - Depending on image size, allow saving to the website or sharing as a temporary link.

## MVP 7 / * : Add optional background Music + Volume bar 
   - (default off, prefer keyboard on/off)
   
## MVP 8 / * : Change user age (app mode)
   - This is to switch between simpler versions of the app, for, say, babies (button press makes a shape appear) versus, say, an older toddler version, where they might select a truck, human, or tree and then click to get those on the screen. 
   - Or it might let the user (or adult) switch between functionality; between, say: 
      - A, which makes keypresses add that letter to a random position on the screen with a random color, and 
      - B, which makes keypresses 'draw' different figures in the same spot, slowly drawing a pre-defined (but invisible) piece of art
      - C, which makes keypresses draw letters sequentially (normal typing), and 
   - etc...

## Other ideas:
   - Light/Dark mode (add to my portfolio, too!)
   - 

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
.

---

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