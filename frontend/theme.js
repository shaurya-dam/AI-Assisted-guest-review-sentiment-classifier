document.addEventListener("DOMContentLoaded", () => {
    const switcherBtn = document.getElementById("theme-switcher");

    // 1. Check browser history memory on document boot-up
    if (localStorage.getItem("theme") === "dark") {
        document.documentElement.classList.add("dark");
        if (switcherBtn) switcherBtn.textContent = "🌙 Dark Mode";
    } else {
        document.documentElement.classList.remove("dark");
        if (switcherBtn) switcherBtn.textContent = "☀️ Light Mode";
    }

    // 2. Click execution listening event
    if (switcherBtn) {
        switcherBtn.addEventListener("click", () => {
            document.documentElement.classList.toggle("dark");

            if (document.documentElement.classList.contains("dark")) {
                localStorage.setItem("theme", "dark");
                switcherBtn.textContent = "🌙 Dark Mode";
            } else {
                localStorage.setItem("theme", "light");
                switcherBtn.textContent = "☀️ Light Mode";
            }
        });
    }
});