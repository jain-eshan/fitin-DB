import React from "react";

export default function App() {
  return (
    <div className="min-h-screen flex flex-col bg-gradient-to-tr from-white to-blue-50">
      {/* Header */}
      <header className="w-full py-6 px-4 flex items-center justify-between border-b border-blue-100 bg-white/80 backdrop-blur sticky top-0 z-10">
        <span className="text-2xl font-extrabold tracking-tight text-blue-700">Fitin Club</span>
        <nav className="space-x-6 text-sm font-medium text-blue-700">
          <a href="#features" className="hover:underline">Features</a>
          <a href="#join" className="hover:underline">Join</a>
          <a href="#login" className="hover:underline">Login</a>
        </nav>
      </header>

      {/* Hero Section */}
      <main className="flex-1 flex flex-col items-center justify-center text-center px-4 py-20">
        <h1 className="text-4xl sm:text-5xl font-black text-blue-800 mb-4 leading-tight">
          Become the Best Version of You
        </h1>
        <p className="text-lg sm:text-xl text-blue-600 mb-8 max-w-xl mx-auto">
          Welcome to Fitin Club — your all-in-one fitness community. Track workouts, log meals, join challenges, and connect with coaches. Minimal. Powerful. Made for you.
        </p>
        <a href="#join" className="inline-block bg-blue-700 text-white font-semibold py-3 px-8 rounded-full shadow hover:bg-blue-800 transition">
          Join Fitin Club
        </a>
      </main>

      {/* Features Section */}
      <section id="features" className="py-16 px-4 bg-white border-t border-blue-100">
        <div className="max-w-4xl mx-auto grid grid-cols-1 sm:grid-cols-2 gap-10">
          <div className="flex flex-col items-center text-center">
            <span className="text-blue-700 text-4xl mb-2">💪</span>
            <h3 className="font-bold text-lg mb-1">Personalized Routines</h3>
            <p className="text-blue-600 text-sm">Get custom workout plans crafted by real coaches for real results.</p>
          </div>
          <div className="flex flex-col items-center text-center">
            <span className="text-blue-700 text-4xl mb-2">🥗</span>
            <h3 className="font-bold text-lg mb-1">Diet & Meal Logging</h3>
            <p className="text-blue-600 text-sm">Log your meals and macros with ease. Nutrition made simple.</p>
          </div>
          <div className="flex flex-col items-center text-center">
            <span className="text-blue-700 text-4xl mb-2">📅</span>
            <h3 className="font-bold text-lg mb-1">Calendar & Progress</h3>
            <p className="text-blue-600 text-sm">Visualize your journey. Stay motivated with streaks and stats.</p>
          </div>
          <div className="flex flex-col items-center text-center">
            <span className="text-blue-700 text-4xl mb-2">🤝</span>
            <h3 className="font-bold text-lg mb-1">Community & Support</h3>
            <p className="text-blue-600 text-sm">Connect with members, join challenges, and grow together.</p>
          </div>
        </div>
      </section>

      {/* Join Section */}
      <section id="join" className="py-20 px-4 flex flex-col items-center bg-blue-50 border-t border-blue-100">
        <h2 className="text-2xl font-bold text-blue-800 mb-4">Ready to Transform?</h2>
        <p className="text-blue-600 max-w-lg mb-8">Sign up now and get access to all features. No fluff, no distractions. Just results.</p>
        <form className="w-full max-w-sm flex flex-col gap-4">
          <input type="email" placeholder="Your email" className="rounded px-4 py-3 border border-blue-200 focus:ring-2 focus:ring-blue-300 outline-none" required />
          <input type="password" placeholder="Password" className="rounded px-4 py-3 border border-blue-200 focus:ring-2 focus:ring-blue-300 outline-none" required />
          <button type="submit" className="bg-blue-700 text-white font-bold py-3 rounded shadow hover:bg-blue-800 transition">Create Account</button>
        </form>
      </section>

      {/* Footer */}
      <footer className="py-8 text-center text-blue-400 text-xs bg-white border-t border-blue-100">
        &copy; {new Date().getFullYear()} Fitin Club. Built for the bold.
      </footer>
    </div>
  );
}
