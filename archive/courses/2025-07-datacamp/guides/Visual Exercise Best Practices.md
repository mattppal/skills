# Visual Exercise Best Practices

Visual exercises are a powerful way to demonstrate tools, workflows, and concepts in action. They pair a **video or image** with an **interactive multiple-choice question (MCQ)**, helping learners observe, interpret, and apply what they’ve seen. A good example of a [visual exercise can be found here](https://campus.datacamp.com/courses/introduction-to-microsoft-copilot/overview-of-microsoft-copilot?ex=9).

  

![](https://t24474497.p.clickup-attachments.com/t24474497/52a27fb7-e72a-45b0-a382-9b58a068a8fc/image.png)

  

These are ideal for:

*   Demonstrating interfaces (e.g., GitHub Copilot, Windsurf, etc...)
*   Showing behavior (e.g., AI assistant completion flow, errors and fixes)
*   Guiding learners through real-world code editing or debugging flows

## The Anatomy of a Visual Exercise

Each visual exercise consists of the following components:

*   **Image or video** (side-by-side with the question)
*   **Exercise title** (max 25 characters)
*   **Exercise description** (includes narrative context; see [Storytelling Guidelines](http://#))
*   **Exercise instructions** (bulleted)
*   **Exercise hints** (bulleted and helpful but non-revealing)
*   **MCQ question** with 3–4 answer options (one correct, others plausible)

## Best Practices for Sharing Videos

**Write a clear script beforehand**

*   The script should focus on solving the learning objective of the exercise.
*   Avoid filler—keep the flow purposeful and concise.
*   Include your script in your deliverables (for closed captioning).

  

**Record with high visual quality**

*   Use [ScreenStudio](https://screenstudio.app/) or Cleanshot for high-res recordings.
*   Ensure your screen is uncluttered and font sizes are readable.
*   Use light or dark mode consistently throughout your course.
*   To time your audio, you can read the script while performing visual actions — the DataCamp team will replace your audio with a higher definition audio

  

**Share the setup instructions for replication**

You must include replication steps if your demo requires replicating an environment (e.g., VS Code with a specific tool, or a dataset/code combo)**. Include the following:**

  

*   **Dataset link or source**
    *   If using a public dataset, provide the direct URL.
    *   For custom data, provide the CSV/JSON file
*   **Tooling setup**
    *   Name and version of tools or extensions (e.g., Copilot v1.170, Cursor IDE)
    *   Installation instructions or links
    *   Any setup commands (e.g., `pip install`, `npm install`, `conda env create`)
*   **Codebase or repo used**
    *   Share a GitHub or Workspace link with preloaded scripts or notebooks
    *   Include any necessary config files or terminal setup steps
*   **Actions demonstrated**
    *   Clearly document the exact steps you took (e.g., “Open [`main.py`](http://main.py), invoke Copilot with Cmd+Enter, accept suggestion, run script.”)

## Writing the MCQ Question

*   Ensure the question **directly tests something visible or inferable from the video/image**.
*   Use plausible distractors that reflect common mistakes or misconceptions.
*   Test observation, comprehension, or conceptual reasoning—not just recall.

  
  
###