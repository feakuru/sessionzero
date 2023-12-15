# session0

This project is intended to help TTRPG players and game masters with managing their campaign expectations, wants, hopes, dreams and wishes. Putting it into more concrete terms, it is indended for managing a type of pre-campaign discussion that a lot of DMs and GMs out there believe is (or rather, should be) a crucial part of any campaign, colloquially called a **"Session Zero"** (referring to the fact that it comes right before the actual play sessions - and giving a array-with-zero-starting coding monkey like me a way to feel seen without actually being seen).

## What a session0 contains

Here's a [checklist](https://www.reddit.com/r/dndnext/comments/601awb/session0_topic_checklist_and_guide/) for the questions that can be fit into a quiz/form/smth like that, but here's what can also be done:
1. Character creation - great team activity, but people can prefer to do it alone
2. Basic plot setup, like "you will start the adventure in Barovia, so we can go from a tavern or already on the way there", that kind of stuff
3. Education - it's really cool if I as a GM can send my players YouTube videos for them to never watch

## Considerations before starting

I want to create a way for players and DMs to experience a session0 in a comfortable, remote-positive way, all the while providing sufficient depth to the results thay get out of it. The following possible user scenarios thus are:

- **"home"**: a group of people gathers to have a face-to-face session0. They need something to record the process and results, but otherwise they are going to discuss things in person, in real time.
- **"remote"**: a real-time session0 with some kind of video chat and/or stream as the communication basis.
- **"async"**: a session0 with asynchronous communication as the communication basis, meaning that it happens over a longer period of time (maybe a few days, maybe a month if someone really wants to procrastinate, nothing wrong with that 😈), and the participants need some way of coordinating their prepping efforts.

Also, I need to take into account the following differences in GM styles:
- some people want to discuss everything in detail
- some people want a form to offload most questions to
- some people want to use photos, minis and other physical objects
- some people love VTTs
- some people need a tool to manage characters
- some people like D&D Beyond
- some people want to be able to tell things to characters in private and not have all information be immediately shared

Also, I dream of creating something like a VTT on a completely open source basis, so I'm going to treat this project as a stepping stone towards that, whatever that may mean.

With that, I present to you the

## Project architecture outline

The project will be a web app. Maybe also a Flutter crossplatform native app in the future. We'll see.

1. frontend
    * has to have a clean and understandable UI that will support mobile devices as well as desktops and features as little "viewport discrimination" as possible
    * has to delegate as much functionality as possible to the backend - both to minimize client-side resource consumption and to embrace the async way<sup>TM</sup>
    * JWT, openauth, all that stuff
    * GMs can create have different session0s with different (or same) groups of players, no restrictions on amounts except those set by the GM themself
    * players can join/leave session0s according to privacy settings
    * there are question forms that the GM creates. these need to allow for:
        * pagination
        * rich text blocks
        * opening links/videos in a dedicated iframe
        * question-level anonimity settings 
        * all basic types of questions (re: Google Forms) plus a type for the GM to be able to record the things everyone is saying into a concise form that everyone can agree on
        * a "session log" where users can view the results of the session

2. backend
    * RESTful API to support the abovementioned
    * probs a chat? idk
    * persistent storage, postgres db, we all know how web services go
