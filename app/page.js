"use client";

import { useState } from "react";

export default function Home() {
  const [text, setText] = useState("");

  const saveToFile = () => {
    const blob = new Blob([text], { type: "text/plain" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "clipping.txt";
    a.click();
  };

  return (
    <main className="min-h-screen p-10 bg-gray-900 text-white">
      <h1 className="text-3xl font-bold mb-4">Web Clipping Tool</h1>

      <textarea
        className="w-full h-64 p-4 rounded bg-gray-800 border border-gray-700"
        placeholder="Paste teks / hasil clipping..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />

      <button
        className="mt-4 px-6 py-2 bg-blue-600 rounded hover:bg-blue-700"
        onClick={saveToFile}
      >
        Save to File
      </button>
    </main>
  );
}

