# Spotify Integration Setup 🎵

To make your "Currently Playing on Spotify" widget work, you need to set up Spotify API credentials.

## Step 1: Create Spotify App

1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
2. Log in with your Spotify account
3. Click "Create App"
4. Fill in:
   - **App Name**: `GitHub Profile`
   - **App Description**: `For GitHub profile README`
   - **Redirect URI**: `http://localhost:3000/callback`
5. Check the boxes and click "Create"
6. Copy your **Client ID** and **Client Secret**

## Step 2: Get Refresh Token

1. Go to this URL (replace YOUR_CLIENT_ID with your actual Client ID):
```
https://accounts.spotify.com/authorize?client_id=YOUR_CLIENT_ID&response_type=code&redirect_uri=http://localhost:3000/callback&scope=user-read-currently-playing%20user-read-recently-played
```

2. Log in and authorize the app
3. You'll be redirected to `http://localhost:3000/callback?code=SOME_CODE`
4. Copy the `code` parameter from the URL

5. Use this code to get your refresh token by making a POST request:
```bash
curl -X POST https://accounts.spotify.com/api/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=authorization_code&code=YOUR_CODE&redirect_uri=http://localhost:3000/callback&client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET"
```

6. Copy the `refresh_token` from the response

## Step 3: Add GitHub Secrets

1. Go to your GitHub repository
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret** and add these three secrets:

- **Name**: `SPOTIFY_CLIENT_ID`
  **Value**: Your Client ID from Step 1

- **Name**: `SPOTIFY_CLIENT_SECRET`
  **Value**: Your Client Secret from Step 1

- **Name**: `SPOTIFY_REFRESH_TOKEN`
  **Value**: Your refresh token from Step 2

## Step 4: Test the Workflow

1. Go to your repository → **Actions** tab
2. Click **Spotify Now Playing** workflow
3. Click **Run workflow** to test it
4. The workflow will run every 5 minutes automatically

## Alternative: Simpler Spotify Widget

If the above seems too complex, you can use this simpler approach:

1. Go to [Spotify GitHub Profile](https://spotify-github-profile.vercel.app/)
2. Log in with your Spotify account
3. Copy the generated image URL
4. Replace the current Spotify widget in your README with your personal URL

## Troubleshooting

- Make sure your Spotify app has the correct redirect URI
- Ensure all secrets are added correctly to GitHub
- The widget shows "Not Playing" when you're not listening to music
- It may take a few minutes for changes to appear

That's it! Your Spotify widget should now show your currently playing music! 🎶
