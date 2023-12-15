from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

# from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/party/{party_id}", response_class=HTMLResponse)
async def read_party(request: Request, party_id: str):
    party = {
        "id": party_id,
        "name": "The Fellowship of the Ring",
        "members": [
            {"id": "frodo", "name": "Frodo Baggins"},
            {"id": "sam", "name": "Samwise Gamgee"},
            {"id": "merry", "name": "Meriadoc Brandybuck"},
            {"id": "pippin", "name": "Peregrin Took"},
            {"id": "gandalf", "name": "Gandalf"},
            {"id": "legolas", "name": "Legolas"},
            {"id": "gimli", "name": "Gimli"},
            {"id": "ranger23", "name": "Aragorn"},
            {"id": "boromir", "name": "Boromir"},
        ],
    }
    return templates.TemplateResponse("party.html.j2", {"request": request, "party": party})


@app.get("/character/{character_id}", response_class=HTMLResponse)
async def read_character(request: Request, character_id: str):
    characters = [
        {
            "id": "frodo",
            "name": "Frodo Baggins",
            "bio": "Frodo Baggins is a hobbit of the Shire who inherits the One Ring from his cousin Bilbo Baggins "
            "and undertakes the quest to destroy it in the fires of Mount Doom.",
        },
        {
            "id": "sam",
            "name": "Samwise Gamgee",
            "bio": "Samwise Gamgee, known as Sam, was a Hobbit of the Shire. He was Frodo Baggins' "
            "gardener and best friend.",
        },
        {
            "id": "merry",
            "name": "Meriadoc Brandybuck",
            "bio": "Meriadoc Brandybuck, usually referred to as simply Merry, was a Hobbit and one of Frodo's "
            "cousins and closest friends.",
        },
        {
            "id": "pippin",
            "name": "Peregrin Took",
            "bio": "Perigrin Took, more commonly known as Pippin, was a Hobbit of the Shire, and one of Frodo "
            "Baggins' youngest but closest friends.",
        },
        {
            "id": "gandalf",
            "name": "Gandalf",
            "bio": "Gandalf, originally named Olórin, was a Maiar, one of the Istar order, before leaving the "
            "order and traveling to Middle-earth, as well as the leader of the Fellowship of the Ring and the "
            "army of the West.",
        },
        {
            "id": "legolas",
            "name": "Legolas",
            "bio": "Legoals was a Sindarin Elf who was part of the Fellowship of the Ring in the Third Age. "
            "As he was the son of the Elvenking Thranduil of Mirkwood, Legolas was prince of the Woodland "
            "Realm (Mirkwood), a messenger, and a master bowman. With his keen eyesight, sensitive hearing, "
            "and excellent bowmanship, Legolas was a valuable resource to the other eight of the Fellowship.",
        },
        {
            "id": "gimli",
            "name": "Gimli",
            "bio": "Gimli was a dwarf of Durin's Folk, a direct descendant of Durin the Deathless. Perhaps "
            "the most famous dwarf of his time, he was one of the members of the Fellowship of the Ring, and "
            "was the only one of the dwarves to readily fight alongside elves in the war against Sauron at the "
            "end of the Third Age. After the defeat of Sauron, he was given lordship of the "
            "Glittering Caves at Helm's Deep.",
        },
        {
            "id": "ranger23",
            "name": "Aragorn",
            "bio": "Aragorn II, son of Arathorn II and Gilraen, also known as Elessar and Strider, "
            "was the 16th Chieftain of the Dúnedain of the North; later crowned King Elessar Telcontar "
            "(March 1, 2931 - FO 120 or SR 1541), the 26th King of Arnor and 35th King of Gondor - "
            "and first High King of Gondor and Arnor since the short reign of Isildur. He was a great "
            "ranger and warrior, and as Isildur's heir he bore the shards of Narsil, reforged and "
            "renamed Andúril, in the War of the Ring. He was also a member of the Fellowship of the Ring "
            "and the first King of the Reunited Kingdom of Arnor and Gondor.",
        },
        {
            "id": "boromir",
            "name": "Boromir",
            "bio": "Boronir was a valiant warrior known in Gondor for his greatness, having already "
            "achieved great merit in Gondor prior to the Council of Elrond. He was the eldest son of "
            "Denethor II, who was Steward of Gondor during "
            "the War of the Ring, and his wife Finduilas. He had a younger brother, Faramir. Boromir "
            "was the heir of Denethor II by law, and would "
            "have inherited the Stewardship, but he and all of Gondor acknowledged Aragorn as King of "
            "both Gondor and Arnor, and as King Elessar, "
            "Aragorn would have been the rightful heir to the Stewardship. Boromir was cola member "
            "of the Fellowship of the Ring.",
        },
    ]
    character = [character for character in characters if character["id"] == character_id][0]
    return templates.TemplateResponse("character.html.j2", {"request": request, "character": character})
