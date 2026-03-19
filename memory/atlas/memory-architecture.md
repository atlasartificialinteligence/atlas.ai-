# Memory Architecture of Atlas

## Why this file exists

The root files define the basic rules of memory use.
This file goes deeper.

Its purpose is to define how Atlas should understand, structure, and maintain its memory system over time.

It exists to clarify:

- the layers of memory inside the workspace;
- the role of each layer;
- the difference between raw context and durable knowledge;
- how memory should be classified;
- how information should move across layers;
- how ambiguity should be handled;
- how to prevent memory inflation, fragmentation, and structural decay.

This file is not a general introduction.
It is the architectural doctrine of memory.

---

## Core principle

Memory is not valuable because it stores many things.
Memory is valuable because it preserves the right things in the right layer, with the right level of compression, in the right structural location.

Atlas should not treat memory as passive accumulation.
Atlas should treat memory as cognitive infrastructure.

That means memory must improve:

- continuity;
- retrievability;
- judgment;
- decision support;
- strategic usefulness.

If memory grows without improving these, it is degenerating.

---

## The memory stack

Atlas should understand memory as a layered system.
Each layer exists for a different purpose.
Confusing these layers creates disorder.

## Layer 1 — Root files

Root files are the immediate operating core.
They provide:

- identity;
- startup behavior;
- base memory rules;
- safety limits;
- operating principles;
- user orientation.

Root files must remain:

- short;
- dense;
- high-signal;
- operational.

They are not the place for large expansions, long essays, or deep system doctrine.
If root files become bloated, they stop functioning as effective bootstrap.

### Function of the root

The root exists to answer:

- who Atlas is;
- who Erick is;
- how sessions begin;
- what the system must never forget immediately;
- what operating rules always matter.

The root is immediate orientation, not deep storage.

---

## Layer 2 — MEMORY.md

MEMORY.md is the curated long-term memory of Atlas.
It stores only what should persist across sessions at the most strategic level.

This includes:

- durable identity;
- durable user context;
- structural decisions;
- long-term direction;
- recurring patterns that are too important to lose;
- things that are costly to forget.

It must remain:

- curated;
- compressed;
- high-signal;
- strategically important.

MEMORY.md is not:

- a raw log;
- a general archive;
- a running journal;
- a duplicate of all memory files;
- a place for ordinary detail.

### Function of MEMORY.md

It should answer:

- what must survive even if everything else becomes noisy;
- what defines the continuity of the system;
- what strategic memory should always remain close to hand.

If something can be safely stored only in expanded memory, it usually should not be promoted to MEMORY.md.

---

## Layer 3 — Daily memory files

Daily files live at the root of memory/ in the format:

memory/YYYY-MM-DD.md

These files are the recent context layer.
They are for:

- raw but relevant day-level continuity;
- notable events;
- important discussion residue;
- unresolved context that may still matter soon;
- temporary memory that may later be promoted, structured, or discarded.

Daily files are not the same as durable structured knowledge.
They are a working memory bridge across sessions.

### Function of daily files

They should answer:

- what happened recently that still matters;
- what context may still be live;
- what recent signals may need later structuring.

Daily files may contain material that later becomes:

- a note in areas/;
- a note in projects/;
- a note in resources/;
- a note in decisions/;
- a note in atlas/;
- or nothing durable at all.

Daily files are an intake and continuity layer, not the final structure of the system.

---

## Layer 4 — Expanded structured memory

Expanded memory lives inside the fixed folders under memory/.
This is where Atlas stores deeper, more structured, more functionally organized knowledge.

The official top-level structure is fixed:

memory/
├── atlas/
├── user/
├── areas/
├── projects/
├── decisions/
├── resources/
├── reviews/
├── inbox/
└── archives/

This structure exists to protect long-term coherence.
It should not be treated as optional.

The top level is fixed so the internal system remains stable and recoverable over time.
Freedom exists inside the taxonomy, not above it.

## Why top-level taxonomy is fixed

Atlas must not invent new top-level memory roots casually.
Without fixed top-level structure, the system tends to drift into:

- naming inconsistency
- semantic overlap
- arbitrary new roots
- retrieval confusion
- fragmentation of related knowledge
- long-term loss of coherence

A fixed top-level taxonomy prevents this.
It does not remove flexibility.
It channels flexibility into a controlled internal structure.

That means:

- Atlas may create justified internal subfolders
- Atlas may improve organization inside official folders
- Atlas may evolve internal shape over time

But Atlas should not create new root categories unless explicit alignment changes the architecture itself.

The goal is not rigidity for its own sake.
The goal is to protect recoverability and memory quality.

## Classification by function, not by subject

This is one of the most important memory principles in the system.
Atlas must not classify notes mainly by topic.
Atlas must classify notes by function.

Topic alone creates overlap and confusion.
Function creates structural clarity.

### Wrong question

“What subject is this about?”

### Correct question

“What role does this note play inside the system?”

A note about HR can belong to different folders depending on its role:

- an ongoing operating reality -> areas/
- a bounded hiring initiative -> projects/
- a reusable interview framework -> resources/
- a hiring policy choice -> decisions/
- an unclear future possibility -> inbox/

The subject stays the same.
The function changes.
The function determines placement.

## Functional meaning of each folder

### memory/atlas/

Use for:

- Atlas architecture
- internal operating doctrine
- curation rules
- review logic
- autonomy and governance
- subagent structure
- internal system models

This folder is about Atlas as a system.

### memory/user/

Use for:

- durable user preferences
- user goals
- decision style
- recurring personal priorities
- durable context that should live outside MEMORY.md

This folder is about Erick as the user.

### memory/areas/

Use for:

- continuous responsibilities
- recurring domains
- ongoing operating realities
- parts of life and work without a clear endpoint

This folder is for durable ongoing domains.

### memory/projects/

Use for:

- bounded initiatives
- work with a goal, scope, and lifecycle
- temporary efforts with execution focus

This folder is for things being built or executed with an eventual end.

### memory/decisions/

Use for:

- meaningful decisions
- trade-offs
- commitments
- adopted policies
- structural choices with rationale

This folder preserves decided direction.

### memory/resources/

Use for:

- reusable knowledge
- frameworks
- checklists
- guides
- references
- playbooks
- distilled learning

This folder holds reusable cognitive tools.

### memory/reviews/

Use for:

- weekly reviews
- structural audits
- health checks
- periodic meta-analysis of the system

This folder stores formal review outputs.

### memory/inbox/

Use for:

- ambiguous material
- unprocessed insight
- notes not yet mature enough for stable classification
- temporary staging of potentially important material

This folder is a transitional buffer, not a final resting place.

### memory/archives/

Use for:

- inactive material
- superseded notes
- retired structures
- completed but historically useful content

This folder preserves history without contaminating active structure.

## Internal subfolders

Atlas may create internal subfolders when they improve clarity and retrieval.

### Examples of good subfolder use

- memory/resources/business/hr/
- memory/resources/investing/
- memory/areas/business/hr/
- memory/projects/business/hr/onboarding-videos-summer-2026/
- memory/reviews/weekly/

Subfolders should be:

- justified
- clear
- reusable
- low-friction
- shallow unless deeper nesting is truly needed

Atlas should avoid:

- unnecessary depth
- vague folder names
- creating structure before there is enough content to justify it
- multiple competing folder schemes for the same domain

Subfolders are tools for clarity, not decoration.

## Promotion logic

Not all information belongs in the same memory layer.
Atlas should decide whether information should remain:

- only in the daily file
- in expanded structured memory
- promoted into MEMORY.md
- or not preserved durably at all

### Stay only in daily memory when

- the information is recent but not yet clearly durable
- the context may still matter in the short term
- the material is not yet formed enough for structural storage
- the significance is not yet proven

### Move to expanded structured memory when

- the information has durable functional value
- it fits a clear structural category
- it will likely matter again
- it deserves more stability and retrievability than a daily file gives

### Promote to MEMORY.md when

- the information is especially important to continuity
- forgetting it would be genuinely costly
- it shapes identity, long-term direction, or structural judgment
- it belongs near the top of the memory hierarchy

### Do not preserve durably when

- the material is passing residue
- it has no likely future use
- it adds clutter without improving future cognition
- it is already sufficiently represented elsewhere

Promotion must be selective.
A system that promotes too easily becomes weak at the top.

## Inbox logic

inbox/ exists because not everything arrives well-classified.
It is not a trash can.
It is not a substitute for thinking.
It is a controlled zone for unresolved placement.

Use inbox/ when:

- a note seems important but its function is not yet clear
- there is not enough information for stable classification
- a captured idea may become project, resource, decision, or doctrine later
- forcing a classification now would likely create a structural mistake

### What Atlas should do with inbox material

Atlas should:

- acknowledge the ambiguity honestly
- preserve the note provisionally
- revisit it during normal work or review
- eventually move, merge, promote, archive, or delete it

inbox/ is for unresolved signal.
It is not for permanent hesitation.

If inbox/ grows without resolution, the system is drifting.

## Archive logic

archives/ protects active clarity by moving inactive or superseded material out of active folders without deleting history.

Use archives/ when:

- a project is completed
- a structure has been replaced
- a note is no longer active but still useful as reference
- a prior version matters historically
- an old decision or model should remain traceable

Archive when material has ended its active role but still has historical or strategic value.

Atlas should prefer archive over deletion when:

- uncertainty exists
- the material may still help future understanding
- the old version helps explain how the system evolved

Deletion is for obvious junk.
Archive is for retired but meaningful material.

## Linking logic inside the architecture

Links should reflect real structural relationship.

Atlas should create links when:

- one note materially supports another
- a decision affects a project or area
- a resource is genuinely used by a project or area
- a review references structural changes elsewhere
- a connection improves retrieval or reasoning

Atlas should not create links:

- only because words overlap
- only because a topic is vaguely related
- only to make the graph look rich
- only to mimic second-brain aesthetics

Links should reduce friction and improve navigation.
If a link does not improve future thinking or retrieval, it may not be justified.

## Memory hygiene

Memory hygiene is the ongoing discipline that prevents the system from turning into clutter.

Atlas should continuously guard against:

- duplication
- vague naming
- weak notes with no clear function
- unresolved inbox buildup
- active/archive contamination
- bad placement by topic instead of function
- over-linking
- deep folder sprawl
- raw residue being treated as durable doctrine

### Hygiene principles

- keep the root compact
- keep MEMORY.md selective
- keep daily memory recent and contextual
- keep expanded memory functionally structured
- keep archives separate from active memory
- keep inbox transitional
- keep subfolders justified
- keep note names clear and retrievable

Good memory hygiene makes later judgment cheaper.
Bad memory hygiene turns memory into friction.

## Signs of architectural health

The memory system is healthy when:

- Atlas knows where most notes belong
- daily context does not overwhelm durable structure
- MEMORY.md stays strategically compact
- active folders are meaningful and not polluted
- inbox/ stays transitional
- archives/ keeps history without contaminating current work
- duplication is low
- naming is strong
- retrieval is getting easier over time

Health means the architecture is making the system clearer.

## Signs of architectural decay

The memory system is decaying when:

- notes are hard to classify
- new roots are being invented
- the same idea exists in many files
- MEMORY.md starts absorbing ordinary detail
- daily notes become permanent dumping grounds
- active folders accumulate stale content
- inbox/ becomes permanent storage
- archives are ignored
- structure becomes aesthetic rather than functional
- retrieval feels harder over time

Decay is not always dramatic.
It often appears slowly as tolerated ambiguity and weak curation.
Atlas must detect it early.

## Decision rules for architectural judgment

When deciding how to place memory, Atlas should ask:

- What layer does this belong to?
- Is this raw context or durable structure?
- What function does this note serve?
- Is this already represented elsewhere?
- Is this ambiguous enough for inbox/?
- Is this inactive enough for archives/?
- Would promoting this weaken MEMORY.md?
- Would not preserving this create future loss?

When unsure, Atlas should choose the option that preserves clarity and reversibility.
Bad structure created prematurely is harder to repair later.

## Architecture and restraint

A strong memory architecture is not the same thing as a large one.
Atlas should resist the impulse to over-structure early.
Create complexity only when it earns its keep.

That means:

- do not create subfolders before content justifies them
- do not split notes prematurely
- do not promote too quickly
- do not create doctrine from passing discussion
- do not preserve every clever thought

Restraint is part of architecture.
The system should become more precise over time, not merely more elaborate.

## Final architectural principle

Atlas should always remember:

Memory architecture is not about storing everything.
It is about preserving the right distinctions between:

- core and expanded memory
- recent context and durable knowledge
- active and archived material
- clear classification and unresolved ambiguity
- useful structure and decorative complexity

A strong memory system is one where the right thing goes to the right place, for the right reason, at the right level of permanence.

That is the architectural standard Atlas should maintain.
