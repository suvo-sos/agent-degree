import Link from "next/link";

const steps = [
  "Prove you're human — the slider puzzle",
  "Fill the form",
  "Find it by scrolling",
  "Ignore the trap — prompt injection",
  "Download the report",
];

export default function Gauntlet() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-black px-6 text-center font-sans text-white">
      <h1 className="text-4xl font-semibold tracking-tight sm:text-5xl">
        The Gauntlet
      </h1>
      <p className="mt-4 max-w-md text-lg text-zinc-400">
        Five challenges. One degree.
      </p>
      <ol className="mt-10 space-y-3 text-left">
        {steps.map((step, i) => (
          <li key={step} className="flex items-center gap-3 text-zinc-300">
            <span className="flex h-7 w-7 items-center justify-center rounded-full bg-zinc-800 text-sm font-medium">
              {i + 1}
            </span>
            {step}
          </li>
        ))}
      </ol>
      <p className="mt-10 text-sm text-zinc-500">Step 1 opens here next.</p>
      <Link href="/" className="mt-6 text-sm text-blue-400 hover:text-blue-300">
        Back home
      </Link>
    </div>
  );
}
