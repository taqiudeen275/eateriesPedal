let nav = document.querySelector('nav')
let menubtn = document.querySelector('.menu-toggle')
let menuicon = document.querySelector('.menu-icon')

menubtn.addEventListener('click',()=>{
    nav.classList.toggle('menuActive')
    menuicon.classList.toggle('active')
})
window.addEventListener('load', load())
function load(){
    loadingBg = document.querySelector('.loading-bg')
    loadingBg.style.visibility = 'visible'
    setTimeout(removeLoader, 2000)
}
function removeLoader(){
    loadingBg = document.querySelector('.loading-bg')
    loadingBg.style.visibility = 'hidden'
}