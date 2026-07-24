// ============================================================
// NovaStart — main.js
// Handles: mobile nav toggle + async contact form submission
// ============================================================

// --- CONFIG ---------------------------------------------------
// During local dev this points at your local Flask server.
// After deploying the backend (see README), replace this with
// your live backend URL, e.g. "https://novastart-api.onrender.com"
const API_BASE_URL = "https://startup-portfolio-api.onrender.com";const INTAKE_ENDPOINT = `${API_BASE_URL}/api/contact`;

// --- MOBILE NAV -------------------------------------------------
const burgerBtn = document.getElementById("burgerBtn");
const mobileMenu = document.getElementById("mobileMenu");

burgerBtn.addEventListener("click", () => {
  const isOpen = mobileMenu.classList.toggle("open");
  burgerBtn.setAttribute("aria-expanded", String(isOpen));
});

mobileMenu.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => {
    mobileMenu.classList.remove("open");
    burgerBtn.setAttribute("aria-expanded", "false");
  });
});

// --- CONTACT FORM -------------------------------------------------
const form = document.getElementById("intakeForm");
const submitBtn = document.getElementById("submitBtn");
const statusEl = document.getElementById("formStatus");

function setStatus(message, state) {
  statusEl.textContent = message;
  statusEl.dataset.state = state || "";
}

function setLoading(isLoading) {
  submitBtn.disabled = isLoading;
  submitBtn.querySelector(".btn__label").textContent = isLoading
    ? "Submitting…"
    : "Submit intake";
}

form.addEventListener("submit", async (event) => {
  event.preventDefault(); // stop the browser's default full-page reload/POST

  // Basic client-side validation (defense-in-depth — the server re-checks this too)
  const name = form.name.value.trim();
  const email = form.email.value.trim();
  const message = form.message.value.trim();

  if (!name || !email || !message) {
    setStatus("Please fill in your name, email, and project details.", "error");
    return;
  }

  const payload = {
    name,
    email,
    company: form.company.value.trim(),
    budget: form.budget.value,
    message,
  };

  setLoading(true);
  setStatus("Sending your intake…");

  try {
    const response = await fetch(INTAKE_ENDPOINT, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    // The server always replies with JSON — even on errors — so we parse
    // it before checking response.ok, to surface a useful message either way.
    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.error || "Something went wrong. Please try again.");
    }

    setStatus("Thanks — your intake was received. We'll reply within 24 hours.", "success");
    form.reset();
  } catch (err) {
    console.error("Intake submission failed:", err);
    setStatus(
      "We couldn't reach the server. Check your connection and try again.",
      "error"
    );
  } finally {
    setLoading(false);
  }
});