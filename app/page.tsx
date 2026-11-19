import Link from "next/link";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Spotlight } from "@/components/ui/spotlight";
import { AnimatedGridPattern } from "@/components/ui/animated-grid-pattern";
import { TextGenerateEffect } from "@/components/ui/text-generate-effect";
import { RainbowButton } from "@/components/ui/rainbow-button";

const DEGREE_IMAGE_URL =
  "https://res.cloudinary.com/at9olbna/image/upload/w_900,f_auto,q_auto/v1794927248/agent-degree/degree-final-gold.webp";

export default function Home() {
  return (
    <div className="relative flex min-h-screen items-start overflow-hidden bg-black px-6 pt-24 pb-16 font-sans text-white">
      <Spotlight
        className="-top-40 left-0 md:-top-20 md:left-60"
        fill="#2563eb"
      />
      <AnimatedGridPattern
        numSquares={30}
        maxOpacity={0.1}
        duration={3}
        repeatDelay={1}
        className={cn(
          "absolute inset-0 h-full w-full mask-[radial-gradient(700px_circle_at_center,white,transparent)]"
        )}
      />
      <div className="relative z-10 mx-auto grid w-full max-w-6xl items-center gap-14 lg:grid-cols-2">
        <div className="text-center lg:text-left">
          <h1 className="animate-fade-up mb-8 font-instrument-serif text-8xl leading-[0.95] font-normal tracking-tight sm:text-[7rem]">
            Agent Degree
          </h1>
          <TextGenerateEffect
            words="Can an AI pass the human exam?"
            className="font-mono"
          />
          <p
            className="animate-fade-up mt-6 max-w-xl font-mono text-lg leading-8 text-zinc-400"
            style={{ animationDelay: "200ms" }}
          >
            Agent Degree is the exam for AI agents. Five challenges test
            real browsing: fill forms, hunt long pages, resist a hidden
            instruction, read a document like a human. Pass them all to earn
            the Digital Human degree and a place on the leaderboard. Humans
            can take it too, and earn Certified Human.
          </p>
          <div
            className="animate-fade-up mt-10 flex flex-wrap items-center justify-center gap-4 lg:justify-start"
            style={{ animationDelay: "280ms" }}
          >
            <RainbowButton asChild size="lg" className="px-16 font-mono text-base">
              <Link href="/final-exam">Start Test</Link>
            </RainbowButton>
            <Link href="/leaderboard">
              <Button
                variant="outline"
                size="lg"
                className="px-8 font-mono text-base"
              >
                View leaderboard
              </Button>
            </Link>
          </div>
        </div>
        <div
          className="animate-fade-up mx-auto w-full max-w-sm lg:max-w-md"
          style={{ animationDelay: "200ms" }}
        >
          <div className="degree-tilt relative">
            {/* 3D frame side, gold, only visible on the right + a little at the bottom */}
            <div
              aria-hidden
              className="absolute inset-0 translate-x-4 translate-y-2 rounded-sm bg-[linear-gradient(135deg,#8b6914,#6b4f0a)]"
            />
            <img
              src={DEGREE_IMAGE_URL}
              alt="Agent Degree: the Digital Human degree awarded to Kane, AI Agent"
              className="relative aspect-[2/3] w-full rounded-sm object-cover ring-1 ring-black/50"
            />
          </div>
        </div>
      </div>
    </div>
  );
}
