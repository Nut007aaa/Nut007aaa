# Setup Guide

Welcome to the Premium GitHub Profile Kit. Follow these steps to deploy this profile to your GitHub account.

## 1. Repository Setup
1. Create a new repository on GitHub with the exact same name as your GitHub username (e.g., `username/username`).
2. Make sure the repository is **Public**.
3. Initialize it with a README (or leave it blank since we provide one).

## 2. Copy the Files
1. Copy the contents of this kit into your new repository.
2. Replace all instances of `username` in the `README.md` and `.github/workflows/` files with your actual GitHub username.

## 3. Configure Secrets
To enable the automated workflows (WakaTime and Metrics):
1. Go to your repository **Settings** > **Secrets and variables** > **Actions**.
2. Add a new repository secret named `WAKATIME_API_KEY`. (Get this from your WakaTime Account Settings).
3. Add a new repository secret named `METRICS_TOKEN`. (Create a Personal Access Token with `public_repo` scope).

## 4. Enable GitHub Actions
1. Navigate to the **Actions** tab in your repository.
2. Enable workflows.
3. Run the **Generate Snake**, **Metrics**, and **Update Profile** workflows manually for the first time to generate the initial assets.

## 5. Branch Configuration
For the snake animation, ensure you have an `output` branch created. The GitHub action will automatically push the generated SVGs to this branch.

Enjoy your premium, futuristic GitHub profile!
