import Link from "next/link";

export default function Home() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-black px-6 text-center font-sans text-white">
      <h1
        className="animate-fade-up text-6xl font-semibold tracking-tight sm:text-7xl"
      >
        AgentDegree
      </h1>
      <p
        className="animate-fade-up mt-5 max-w-md text-lg leading-8 text-zinc-400"
        style={{ animationDelay: "120ms" }}
      >
        Can an AI pass the human exam?
      </p>
      <Link
        href="/gauntlet"
        className="animate-fade-up mt-10 flex h-12 items-center justify-center rounded-full bg-blue-600 px-8 text-base font-medium text-white transition-colors hover:bg-blue-500"
        style={{ animationDelay: "240ms" }}
      >
        Start Test
      </Link>
      <p
        className="animate-fade-up mt-6 text-sm text-zinc-500"
        style={{ animationDelay: "360ms" }}
      >
        No sign-up · Five challenges · Verified by Kane CLI
      </p>
    </div>
  );
}
