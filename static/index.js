let nav = document.querySelector('nav')
let menubtn = document.querySelector('.menu-toggle')
let menuicon = document.querySelector('.menu-icon')
let dModal = document.querySelector('.dModal-toggle')

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
dModal.addEventListener('click', ()=>{
    modalBg = document.querySelector('.dModal-bg')
    modalBg.style.opacity = 1
    modalBg.style.transform = 'scale(1)'
})
document.querySelector('.dModalClose').addEventListener('click', ()=>{
    modalBg = document.querySelector('.dModal-bg')
    modalBg.style.opacity = 0
    modalBg.style.transform = 'scale(0)'
})
