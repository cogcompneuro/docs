# Contributed talk selection process

*Authored by the [CCN 2026 Programme Committee](#contact-info).*

## Summary

Contributed talks for CCN 2026 are selected from the submitted extended abstracts and proceedings submissions through a multi-phase process to assure high quality, appeal to the CCN audience, and diversity among contributions. In [Phase 1](#phase-1-initial-score-based-selection), reviewer scores on soundness, clarity, and interest, along with their confidence, are combined into an overall ranking that determines the initial pool of candidate papers. In [Phase 2](#phase-2-clustering-and-initial-scoring), the top $2N$ highest-ranked submissions (see [Phase 1](#phase-1-initial-score-based-selection) for more details) are grouped into topic-based clusters. In [Phase 3](#phase-3-main-selection), program committee members with topic expertise then compose contributed talk sessions from these clusters. Talk sessions are composed with the overall attractiveness of the talk session to the CCN audience, reviewer ranking and comments, diversity of topics and approaches (cognitive, computational, neuro), and diversity of representation (institution, gender, geographic) in mind. During Phases 1–3, author names and affiliations are pseudonymized. In [Phase 4](#phase-4-diversity-and-balance-final-control), submissions are deanonymized and final quality controls and diversity checks are conducted. This process aims to ensure a high-quality and inclusive contributed talk program. In [Phase 5](#phase-5-final-selection-and-documentation), the program committee reviews the final talk list for overall program coherence, session organization, and time slot feasibility, and documents the full selection process for transparency.

**Spotlight papers** (new in 2026): Contributed talk sessions are composed for the CCN audience with several criteria in mind (see [§3.1](#31-within-cluster-selection)). This may sometimes lead to highly ranked papers not being selected for a talk. To acknowledge highly ranked papers independently from their selection as a talk, we therefore designate the top 10% of accepted 2-page submissions as ranked by reviewer ratings as Spotlight papers.

## Overview

Contributed talks serve to highlight the submissions that bring the most significant and timely advances to the CCN community. This policy governs the selection of contributed talks from accepted conference submissions to ensure fair, transparent, and diverse representation while maintaining the quality of the presented talks and the integrity of the review process.

## Phase 1: Initial score-based selection

### 1.1 Scoring system

Reviewers are expected to submit three scores for each submission to judge different aspects of each work (see review form for [Proceedings](../Proceedings/Reviewer%20guidelines.md#review-content) and [Extended Abstracts](../Extended%20Abstracts/Reviewer%20guidelines.md#review-content)):

1. Soundness
2. Clarity
3. Interest

Each of the scores would be within 1-5, with 1 and 5 corresponding to very weak and very strong scores, respectively. In addition, each reviewer would submit a Confidence/Expertise score reflecting their understanding of the submission and related literature.

The overall score is calculated as the average of the soundness, clarity, and interest scores. Let $c_i \in \{1, \dots, 5\}$ and $s_i \in \{1, \dots, 5\}$ denote the confidence and overall score from reviewer $i$, respectively, and let $N$ denote the number of reviewers for a given submission. The final submission score is the overall score aggregated across reviewers, weighted by a softmax of their confidences:

$$ s_{\text{final}} = \sum_{i=1}^{N} w_i \, s_i~, \quad \text{where} \quad w_i = \frac{\exp(c_i)}{\sum_{j=1}^{N} \exp(c_j)}~. $$

### 1.2 Objective

Reduce the full submission pool to a manageable subset for detailed program committee evaluation while maintaining objectivity and reducing the workload for Program Chairs.

### 1.3 Selection criteria

* **Prerequisite:**
    1. Submissions that break the anonymity condition are first removed from the pool.
    2. All submissions are anonymized (by removing the author field from the database).
* **Primary metric:** Average overall reviewer scores across all submissions.
* **Target size:** Select top $\sim\!2N$ submissions (approximately twice the number of available talk slots, $N$). In case at the bottom of the $\sim\!2N$ list we end up with equal average scores, we include all abstracts with equal scores.
* **Top 10%** of all 2-page submissions are selected as **Spotlight** presentations.

### 1.4 Documentation

* Document any exceptions made to the score-based filtering.

## Phase 2: Clustering and initial scoring

### 2.1 Submission clustering

* **Objective:** Group submissions into thematic clusters to enable specialized evaluation.
* **Process:** Cluster submissions by research area, methodology, or topic. This should be done based on the abstracts of the submissions, using a method that is privacy-conscious. An LLM with privacy guarantees may be used to cluster **based on content**.
* The Chair or a delegate will check if the clusters are broadly representative, and reassign submissions that are a better fit for a different cluster.

### 2.2 Program committee assignment

Multiple program chairs will be assigned to each topic cluster to form a cluster committee. The committee's role is to select a balanced set of contributed talks for that topic cluster. The selection is governed by the following guidelines:

* **Conflict-free assignment:** No PC member may be assigned to evaluate a cluster containing submission(s) listing them as co-authors.
* **Balanced expertise:** Each cluster should have 2-4 PC members with relevant domain expertise. In cases where the PC does not have enough experts in each cluster (e.g., due to conflict of interest), PC either recruits from PC members who did not take the review role or externally. It is important that talk selections are made by experts.

### 2.3 Blinded evaluation

* **Anonymization:** All author information, affiliations, and identifying details are removed from submissions during cluster evaluation.
* The following information will be **pseudonymized** (replaced by artificial identifiers), as it will be needed for the [main selection](#phase-3-main-selection) and [balancing phase](#phase-4-diversity-and-balance-final-control) of the selection process.
    * Affiliation of the first (presenting) author.
    * Name of the last author.
    * The country where the first (presenting) author is based.
* **Information on gender and underrepresented group(s):** Presenting authors will be asked to state gender and whether they consider themselves a part of any underrepresented group(s) on their [ccneuro.org](https://ccneuro.org) profile. They may select from the provided predefined options (including "prefer not to say") and, if applicable, provide additional information in a free-text field if their group is not listed. This information will be used during Phase 3 selection.

## Phase 3: Main selection

### 3.1 Within-cluster selection

Each topic cluster committee takes responsibility for selecting the contributed talks within that cluster. The selection process is carried out according to the following guidelines:

* **Process:** First, within each topical cluster, PCs will select candidate talks from the pool of selected extended abstracts (detailed in [Phase 1](#phase-1-initial-score-based-selection)). Subsequently, PC will choose the $N$ talks for the contributed talk sessions from these candidate pools considering all of the following selection criteria:
* **Selection criteria:**
    * **Reviewer scores and comments:** PCs will consider both the scores and the comments on each submission to make their selections (to minimize injecting subjective choices by the cluster committee).
    * **Submission type:** To make sure both early-stage and seasoned trainees will have a chance to present their work as a talk, each committee will select the talks from both the 8-page and 2-page categories according to the ratio between the number of submissions to each category. For instance, if there are 400 and 100 submissions to the 2-page and 8-page paper categories, respectively, 80% of the talks will be selected from the 2-page category and the rest from the 8-page papers.
    * **Diversity of talks:**
        1. **Sex/gender and other self-declared membership of an underrepresented group:** If this information is available for the first author (see [§2.3](#23-blinded-evaluation)), it will be considered in balancing diversity during [Phase 3](#phase-3-main-selection) and [Phase 4](#phase-4-diversity-and-balance-final-control) of contributed talk selection.
        2. **Diversity of disciplinary approaches:** To cover the breadth of computational, cognitive, and neuroscience work (and their combinations).
        3. **Subtopic diversity:** To avoid having two or more talks that are topically or conceptually very close to each other.
        4. **Lab diversity:** Not being from a lab that is already selected for a talk in another cluster.
        5. **Geographic/institution diversity:** Based on pseudonymized affiliations.
        6. **Tie-breaking criteria:**
            1. Not being from the same lab as a keynote speaker.
            2. Not having given a talk during the last CCN.

### 3.2 Preliminary talk list

* Compile an initial list of selected talks from all clusters.
* Document selection rationale for each chosen submission.

## Phase 4: Diversity and balance final control

In Phase 4, submissions are unblinded. Phase 4 serves as a final check to ensure diversity and fairness in the final list of contributed talks across clusters. In case adjustments have to be made, high-scoring alternative submissions will be used as substitutions. Adjustments will be conducted jointly by the PC committee together with representatives of the DEI committee and documented.

## Phase 5: Final selection and documentation

### 5.1 Final review

PC committee reviews final selection for:

* Overall program coherence.
* Time slot feasibility.
* Session organization potential.

### 5.2 Documentation requirements

Maintain records of:

* Initial cluster assignments and PC member assignments.
* Blinded evaluation scores and rationales.
* Diversity analysis and any adjustments made.
* Final selection justification.

### 5.3 Transparency measures

The DEI committee will compile and publish stats before CCN on:

* Number of submissions by cluster.
* Selection rates by cluster.
* Gender, institutional, and geography diversity metrics.
* Summary statistics showing how reviewer scores vary across demographic groups.
* Aggregate statistics on submissions and selections by gender/geography/institution.
* Providing demographic and institutional diversity statistics for the PC committees.

## Contact info

For questions about the contributed talk selection process, please reach out to the Programme Committee via [info@ccneuro.org](mailto:info@ccneuro.org).
