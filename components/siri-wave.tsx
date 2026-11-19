// Siri-style listening waveform: a row of thin coloured bars that rise
// and fall in sequence, like the Siri glow. Shown at the bottom of the
// current (next to do) challenge card on the Final Exam page.
const SIRI_COLORS = ["#0A84FF", "#BF5AF2", "#FF375F", "#FF9F0A"];

export default function SiriWave({ bars = 28 }: { bars?: number }) {
  return (
    <div
      aria-hidden
      className="pointer-events-none absolute inset-x-0 bottom-0 z-10 flex h-8 items-end justify-center gap-[3px] overflow-hidden pb-1"
    >
      {Array.from({ length: bars }).map((_, i) => (
        <span
          key={i}
          className="siri-wave-bar w-[3px] rounded-full"
          style={{
            backgroundColor: SIRI_COLORS[i % SIRI_COLORS.length],
            animationDelay: `${i * 0.06}s`,
          }}
        />
      ))}
    </div>
  );
}
