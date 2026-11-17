import {
  Pagination,
  PaginationContent,
  PaginationItem,
  PaginationLink,
  PaginationNext,
  PaginationPrevious,
} from "@/components/ui/pagination";

const TOTAL_STEPS = 5;

export function StepPagination({
  current,
  available = 1,
}: {
  current: number;
  /** Highest step whose page exists so far; later steps render disabled. */
  available?: number;
}) {
  const prevHref =
    current > 1 ? `/gauntlet/step-${current - 1}` : "/gauntlet";
  const nextHref =
    current < available ? `/gauntlet/step-${current + 1}` : null;

  return (
    <Pagination>
      <PaginationContent>
        <PaginationItem>
          <PaginationPrevious href={prevHref} className="font-mono" />
        </PaginationItem>
        {Array.from({ length: TOTAL_STEPS }, (_, i) => i + 1).map((n) => (
          <PaginationItem key={n}>
            {n <= available ? (
              <PaginationLink
                href={`/gauntlet/step-${n}`}
                isActive={n === current}
                className="font-mono"
              >
                {n}
              </PaginationLink>
            ) : (
              <PaginationLink
                href="#"
                aria-disabled="true"
                className="pointer-events-none font-mono opacity-40"
              >
                {n}
              </PaginationLink>
            )}
          </PaginationItem>
        ))}
        <PaginationItem>
          {nextHref ? (
            <PaginationNext href={nextHref} className="font-mono" />
          ) : (
            <PaginationNext
              href="#"
              aria-disabled="true"
              className="pointer-events-none font-mono opacity-40"
            />
          )}
        </PaginationItem>
      </PaginationContent>
    </Pagination>
  );
}
