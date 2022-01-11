const modal = document.getElementById("modal")

function show() {
    modal.style.display = "flex"
}

function isModalOn() {
    return modal.style.display === "flex"
}

function close() {
    modal.style.display = "none"
}

const closeBtn = modal.querySelector(".close-area")
closeBtn.addEventListener("click", e => {
    close()
})

modal.addEventListener("click", e => {
    const evTarget = e.target
    if(evTarget.classList.contains("modal-overlay")) {
        close()
    }
})

window.addEventListener("keyup", e => {
    if(isModalOn() && e.key === "Escape") {
        close()
    }
})