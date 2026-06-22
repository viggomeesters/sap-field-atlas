# Go Loop Atlas fill campaign

Use this as the prompt/brief for a `$go-loop designer` or `$go-loop plan` run that fills SAP Field Atlas over multiple bounded slices.

## Goal

Grow SAP Field Atlas by filling source-safe, agent-useful SAP object gaps from the current gap report.

## Target repo

- Repo: `/home/viggo/github/sap-field-atlas`
- Public remote: `https://github.com/viggomeesters/sap-field-atlas`
- Canonical gates:
  - `make check`
  - `make gap-report`

## Go-loop shape

```text
DESIGN → PLAN CHILD SLICES → RUN CHILD 1 → VERIFY → CRITIC → REPAIR/SHIP → REFRESH GAP REPORT → NEXT CHILD
```

## Child-task size

One child task should fill exactly one small vertical slice, for example:

- one transaction + table-access relationship;
- one table + key fields + related tables;
- one field + labels + value source + relationships;
- one template field + canonical mapping;
- one `needs_verification` item promoted with public source refs.

Do not create broad children such as “fill all Material Master”.

## Default campaign policy

```yaml
loop:
  mode: go-loop-plan
  max_attempts_per_child: 5
  child_policy: one_writer_at_a_time
  refresh_gap_report_after_each_child: true
  stop_on:
    - make_check_fails_after_attempt_5
    - public_data_safety_risk
    - proprietary_or_customer_source_required
    - schema_needs_design_change
    - unowned_dirty_repo_state
  pass_condition:
    - child_acceptance_met
    - make_check_passes
    - make_gap_report_runs
    - source_confidence_review_passes
    - graph_links_resolve
    - critic_has_no_blocking_findings
    - commit_pushed
```

## Designer output expected

A `$go-loop designer` run should output:

- target and exact repo path;
- selected gap-report snapshot;
- ordered child slices;
- acceptance per child;
- data files likely touched per child;
- verification commands;
- critic checklist;
- stop policy;
- copy-paste command for execution.

## Critic checklist per child

Before accepting a green child, attack:

- Is the slice too broad or too shallow?
- Did it add isolated objects without graph relationships?
- Did it overclaim `verified` without concrete source refs?
- Did it copy or imply proprietary/customer evidence?
- Did it improve agent answers, or only add inert YAML?
- Did `make gap-report` reflect the expected improvement or reveal a new blocker?

## Example go-loop designer prompt

```text
go-loop designer sap-field-atlas atlas-fill campaign:
Use /home/viggo/github/sap-field-atlas.
Run make gap-report, choose the top 5 highest-value public-safe gaps, decompose into child tasks of one vertical slice each, and design a go-loop plan with max 5 attempts per child.
Use docs/ATLAS_FILL_LOOP.md as the domain protocol.
Hard gates: make check, make gap-report, source/confidence review, no customer/proprietary data, graph links useful.
No GitHub Actions. One child commit at a time.
```

## Example go-loop execution prompt

```text
go-loop plan sap-field-atlas atlas-fill campaign --budget 3h --max-attempts 5 --stop-on-blocker
```

In Viggo's Agent Workflow Lite setup, the durable task/plan/run state belongs in the vault under `system/agent-workflow/`, not in this repository. This repository provides the domain protocol, templates, and gates only.
