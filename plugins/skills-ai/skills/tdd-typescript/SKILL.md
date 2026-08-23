---
name: tdd-typescript
description: Strict test-driven development and type discipline for TypeScript and React — red-green-refactor on every behavior, zero `any`, types derived from values, behavior-level React tests instead of implementation-detail tests. Use this skill whenever writing or refactoring TypeScript/React code under test discipline, when the user says "TDD this", "test-first", "strict types", "no any", "type-safe refactor", asks to refactor TS/React without breaking behavior, or invokes /tdd-typescript. Don't use for non-TypeScript languages or for throwaway scripts where the user explicitly doesn't want tests.
---

# TDD TypeScript — Test-First, Types-First

Two disciplines fused: every behavior enters the codebase through a failing test, and the type system is used as a design tool rather than fought as a linter. Both share one premise — feedback in seconds beats debugging in hours.

## The red-green-refactor loop

For each behavior, in order, no skipping:

1. **Red** — write the smallest test that fails for the *right reason*. Run it and read the failure: "expected 3, got undefined" is the right reason; "cannot find module" means the test harness is broken, fix that first. A test you never saw fail proves nothing — it might pass vacuously forever.
2. **Green** — write the minimum implementation that passes. Resist generality the tests don't demand yet; the next red test earns it.
3. **Refactor** — with everything green, improve structure: extract, rename, collapse duplication. One structural change at a time, suite run after each. Never refactor and change behavior in the same step — when a refactor "needs" a test change, that's a behavior change wearing a disguise; stop and decide which one you're doing.

Tests assert the contract (inputs → observable outputs), never internals (private state, call counts on your own code, mock-everything choreography). A test that breaks when you rename a private method is a tax, not a safety net.

## Type discipline

- **`any` is banned**, including the sneaky forms: `as any`, `@ts-ignore`, `@ts-expect-error` without a linked issue, unvalidated `JSON.parse` results. At trust boundaries use `unknown` and narrow with type guards or a schema validator (zod/valibot if the project has one).
- **Strict config is the floor.** `"strict": true` plus `noUncheckedIndexedAccess`. If the project doesn't have these, surface it — turning them on is its own (very worthwhile) task.
- **Derive, don't duplicate.** Types flow from values: `typeof config`, `ReturnType<typeof fn>`, `z.infer<typeof schema>`, `satisfies` for checked-but-not-widened literals. Hand-maintained mirror types drift; derived types can't.
- **Make illegal states unrepresentable.** Discriminated unions over boolean flags: `{status:'loading'} | {status:'error'; error} | {status:'ok'; data}` instead of `isLoading`/`isError`/`data?` — the impossible combinations stop compiling, which deletes the tests you'd otherwise need.
- **Type errors are design feedback.** When a signature needs three overloads and a conditional type to describe, the *function* is too clever — simplify the design before reaching for type gymnastics. Library-grade generics belong in libraries.

## React specifics

- Test through the user's senses with Testing Library: query by role/label/text, interact with `userEvent`, assert what renders. If a test reaches into component state or instance internals, it's testing the framework, not your product.
- Mock at the network/system boundary (MSW or an injected fetcher), not at the "my own modules" boundary — mocking your own modules glues tests to the current file layout.
- Type props precisely; no `React.FC` with implicit children, no prop-drilling `any`. Event handler types come from React's definitions, not hand-rolled.

## Cadence

Work in commit-sized slices: red → green → refactor → commit (when the user wants commits). Run typecheck (`tsc --noEmit`) with the tests every cycle — it's the fastest test you own. If a quality-gates setup exists in the project, those gates run between slices.
