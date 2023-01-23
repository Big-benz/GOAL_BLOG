
// Drop down menus

let insideNavbar = document.querySelector("#inside-navbar");

const cultureClick = document.querySelector("#culture");

cultureClick.addEventListener("click", function(){

    insideNavbar.classList.toggle("active");

})

let settingsTab = document.querySelector("#settings-tab");

const settingsIcon = document.querySelector("#settings");

settingsIcon.addEventListener("click", function(){

    settingsTab.classList.toggle("active");

});
    
let eplContainer = document.querySelector("#epl-container");

const premierLeague = document.querySelector("#premier");

premierLeague.addEventListener("click", function(){

    eplContainer.classList.toggle("active")

});


let laligaContainer = document.querySelector("#laliga-container");

const laLiga = document.querySelector("#laliga")

laLiga.addEventListener("click", function(){

    laligaContainer.classList.toggle("active")

});
   
const afconContainer = document.querySelector("#afcon-container");

const afconStuff = document.querySelector("#afcon")

afconStuff.addEventListener("click",function(){

    afconContainer.classList.toggle("active")

});



let moreContainer = document.querySelector("#more-container");

let moreStuff =  document.querySelector("#more");

moreStuff.addEventListener("click", function(){

    moreContainer.classList.toggle("active")

});


// Grab element easily

const selectElement = (selector) => {

    const element =  document.querySelector(selector)

    if(element) return element;

    throw new Error(`something went wrong, make sure that ${selector} exists or is typed correctly`)
};

// Open and close search field

const openIcon = selectElement("#search-icon");

const closeIcon = selectElement("#close-icon");

const searchBoxContainer = selectElement("#search-box-container");

openIcon.addEventListener("click", () => searchBoxContainer.classList.add("activated"));

closeIcon.addEventListener("click", () => searchBoxContainer.classList.remove("activated"));





// Light mode and dark mode toggle.

const bodyPage = selectElement("#body");

const sunToggle = selectElement("#theme-toggle-btn");

sunToggle.addEventListener("click", () => bodyPage.classList.toggle("light-theme"));

// Back to button appear and disappear.

vanishButton = () => {

    const toTop = selectElement("#to-top");

    if(this.scrollY > 700){

        toTop.classList.add("active");

    }

    else{

        toTop.classList.remove("active")
    }

}

window.addEventListener("scroll", vanishButton);

const videoContainer = document.querySelector(".video-container-main-video")
const pauseBtn = document.querySelector(".pause-btn")
console.log(pauseBtn)
const playBtn = document.querySelector(".play-btn")
const playAndPause = document.querySelector(".play-and-pause-icons")

function playWithSound(){
    videoContainer.muted = !videoContainer.muted
}

window.addEventListener("DOMContentLoaded", function(){
    videoContainer.pause()
    playWithSound()
})

playBtn.addEventListener("click", function(){
    videoContainer.play()
    pauseBtn.style.display = "block"
    playBtn.style.display = "none"
})

pauseBtn.addEventListener("click", function(){
    videoContainer.pause()
    playBtn.style.display = "block"
    pauseBtn.style.display = "none"
})

videoContainer.addEventListener("mouseenter", function(){
    playAndPause.style.display = "block"
})
videoContainer.addEventListener("mouseleave", function(){
    playAndPause.style.display = "none"
})

playAndPause.addEventListener("mouseenter", function(){
    playAndPause.style.display = "block"
})

