# Introduction to Version Control and Git

## What is VCS?

A Version Control System (VCS) is a tool that tracks changes to your files over time. It allows you to recall specific versions later. Think of it as a highly advanced save button for your code.

Key benefits include:

- Tracking every modification made to the code.
- Collaborating with other developers without overwriting each other's work.
- Reverting files or entire projects back to a previous state.
- Creating isolated branches to test new features safely.

## What is Git?

Git is a free and open source distributed version control system. It was created by Linus Torvalds in 2005 for Linux kernel development. Today, it is the most widely used modern version control system in the world.

Unlike older centralized systems, Git gives every developer a full local copy of the entire project history. This makes it incredibly fast and allows you to work offline.

## How does it work?

Git handles data differently than other systems. Instead of storing a list of file differences, Git takes a snapshot of your entire project at each commit. If files have not changed, Git just stores a link to the previous identical file.

The basic workflow revolves around three main states:

1. **Working Directory:** Where you are currently editing your files.
2. **Staging Area:** A holding zone where you prepare your changes for the next commit.
3. **Local Repository:** Where Git permanently stores your committed snapshots.

Every file in Git is check summed using a SHA-1 hash. This ensures data integrity and means nothing can be changed without Git knowing about it.