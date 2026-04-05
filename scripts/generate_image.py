#!/usr/bin/env python3
"""Generate images via Pollinations.ai (free, no API key). Stdlib only, no pip."""

import json
import sys
import os
import urllib.request
import urllib.error
import urllib.parse

POLLINATIONS_URL = "https://image.pollinations.ai/prompt/{prompt}"


def generate(prompt: str, output_path: str, width: int = 1200, height: int = 900,
             model: str = "flux", seed: int = -1, enhance: bool = True, nologo: bool = True) -> dict:
    """Generate an image from a text prompt via Pollinations.ai."""

    params = {
        "width": str(width),
        "height": str(height),
        "model": model,
        "nologo": "true" if nologo else "false",
        "enhance": "true" if enhance else "false",
    }
    if seed >= 0:
        params["seed"] = str(seed)

    encoded_prompt = urllib.parse.quote(prompt, safe="")
    url = POLLINATIONS_URL.format(prompt=encoded_prompt) + "?" + urllib.parse.urlencode(params)

    # Ensure output dir exists
    out_dir = os.path.dirname(output_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    # Add extension if missing
    base, ext = os.path.splitext(output_path)
    if not ext:
        output_path = base + ".jpg"

    try:
        req = urllib.request.Request(url)
        req.add_header("User-Agent", "visual-forge/0.1.0")
        with urllib.request.urlopen(req, timeout=180) as resp:
            img_data = resp.read()
            with open(output_path, "wb") as f:
                f.write(img_data)
    except urllib.error.HTTPError as e:
        return {"error": f"HTTP {e.code}: {e.reason}"}
    except urllib.error.URLError as e:
        return {"error": f"Network error: {e.reason}"}
    except TimeoutError:
        return {"error": "Request timed out (180s). Try a simpler prompt or smaller size."}

    file_size = os.path.getsize(output_path)
    if file_size < 1000:
        # Probably an error response, not an image
        with open(output_path, "r", errors="ignore") as f:
            content = f.read(500)
        os.remove(output_path)
        return {"error": f"Response too small ({file_size}b), likely error: {content}"}

    return {
        "status": "ok",
        "image": output_path,
        "size_bytes": file_size,
        "width": width,
        "height": height,
        "model": model,
        "prompt_length": len(prompt),
    }


def main():
    if len(sys.argv) < 2:
        print(json.dumps({
            "usage": "generate_image.py <command> [args]",
            "commands": {
                "generate": "generate <prompt> <output_path> [width] [height] [model] [seed]",
                "models": "list available models",
            }
        }, indent=2))
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "models":
        print(json.dumps({
            "models": [
                {"name": "flux", "description": "FLUX.1 — best quality, default"},
                {"name": "flux-realism", "description": "FLUX Realism — photorealistic"},
                {"name": "flux-anime", "description": "FLUX Anime — anime style"},
                {"name": "flux-3d", "description": "FLUX 3D — 3D render style"},
                {"name": "flux-pixel", "description": "FLUX Pixel — pixel art style"},
                {"name": "turbo", "description": "SDXL Turbo — fast, lower quality"},
            ],
            "note": "All models are free, no API key needed"
        }, indent=2))

    elif cmd == "generate":
        if len(sys.argv) < 4:
            print(json.dumps({"error": "Usage: generate_image.py generate <prompt> <output_path> [width] [height] [model] [seed]"}))
            sys.exit(1)

        prompt = sys.argv[2]
        output = sys.argv[3]
        width = int(sys.argv[4]) if len(sys.argv) > 4 else 1200
        height = int(sys.argv[5]) if len(sys.argv) > 5 else 900
        model = sys.argv[6] if len(sys.argv) > 6 else "flux"
        seed = int(sys.argv[7]) if len(sys.argv) > 7 else -1

        result = generate(prompt, output, width, height, model, seed)
        print(json.dumps(result, ensure_ascii=False))
        if "error" in result:
            sys.exit(1)

    else:
        print(json.dumps({"error": f"Unknown command: {cmd}. Available: generate, models"}))
        sys.exit(1)


if __name__ == "__main__":
    main()
