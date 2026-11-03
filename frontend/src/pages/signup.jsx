import { useState } from "react";

const API_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

async function getErrorMessage(response) {
  try {
    const data = await response.json();

    if (Array.isArray(data.detail)) {
      return data.detail
        .map((error) => error.msg || "Invalid input")
        .join(", ");
    }

    return data.detail || data.message || "Unable to create your account.";
  } catch {
    return "Unable to create your account. Please try again.";
  }
}

export default function Signup() {
  const [form, setForm] = useState({
    name: "",
    email: "",
    password: "",
    role: "student",
  });
  const [error, setError] = useState("");
  const [message, setMessage] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);

  function handleChange(event) {
    setForm((currentForm) => ({
      ...currentForm,
      [event.target.name]: event.target.value,
    }));
    setError("");
    setMessage("");
  }

  async function handleSubmit(event) {
    event.preventDefault();
    setError("");
    setMessage("");

    if (form.password.length < 8) {
      setError("Password must be at least 8 characters.");
      return;
    }

    setIsSubmitting(true);

    try {
      const response = await fetch(`${API_URL}/user/create`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form),
      });

      if (!response.ok) {
        throw new Error(await getErrorMessage(response));
      }

      setMessage("Account created successfully. You can now sign in.");
      setForm({ name: "", email: "", password: "", role: "student" });
    } catch (requestError) {
      setError(
        requestError instanceof TypeError
          ? "Unable to connect to the server."
          : requestError.message,
      );
    } finally {
      setIsSubmitting(false);
    }
  }

  return (
    <main className="auth-page">
      <section className="auth-card" aria-labelledby="signup-title">
        <div className="auth-heading">
          <span className="auth-eyebrow">Automated Code Evaluator</span>
          <h1 id="signup-title">Create your account</h1>
          <p>Join the platform and start evaluating code.</p>
        </div>

        <form className="auth-form" onSubmit={handleSubmit}>
          <label htmlFor="signup-name">Full name</label>
          <input
            id="signup-name"
            name="name"
            type="text"
            autoComplete="name"
            minLength="5"
            value={form.name}
            onChange={handleChange}
            placeholder="Your full name"
            required
          />

          <label htmlFor="signup-email">Email</label>
          <input
            id="signup-email"
            name="email"
            type="email"
            autoComplete="email"
            value={form.email}
            onChange={handleChange}
            placeholder="you@example.com"
            required
          />

          <label htmlFor="signup-role">Role</label>
          <select id="signup-role" name="role" value={form.role} onChange={handleChange}>
            <option value="student">Student</option>
            <option value="teacher">Teacher</option>
          </select>

          <label htmlFor="signup-password">Password</label>
          <input
            id="signup-password"
            name="password"
            type="password"
            autoComplete="new-password"
            minLength="8"
            value={form.password}
            onChange={handleChange}
            placeholder="At least 8 characters"
            required
          />

          {error && <p className="form-message form-error" role="alert">{error}</p>}
          {message && <p className="form-message form-success" role="status">{message}</p>}

          <button type="submit" disabled={isSubmitting}>
            {isSubmitting ? "Creating account..." : "Create account"}
          </button>
        </form>

        <p className="auth-footer">
          Already have an account?{" "}
          <a href="/login">Sign in</a>
        </p>
      </section>
    </main>
  );
}