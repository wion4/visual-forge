---
name: Visual Forge
description: Use when creating 2D game art, concept art, character designs, environment art, UI design, maps, icons, logos, mood boards, color palettes, or any visual content for games. Also triggers on "draw", "sketch", "concept art", "character design", "environment art", "UI mockup", "map", "icon", "logo", "visual style", "art direction", "color palette", "composition".
version: 0.1.0
---

# Visual Forge — Visual Art Methodology for AI-Generated Game Art

A comprehensive visual art system teaching composition, anatomy, color, light, perspective, and style. Every SVG shape and HTML canvas stroke should follow these principles.

## Language

Detect user's system language via `echo $LANG`. All annotations, labels, and design notes in that language.

## Source Material Reference

This methodology is distilled from masters across painting, illustration, animation, and game art. When applying a technique, reference its origin.

### Classical Painting & Drawing
| Master | Key Techniques |
|--------|---------------|
| Leonardo da Vinci | Anatomical proportion (Vitruvian Man), sfumato (soft edges), atmospheric perspective, golden ratio in composition |
| Michelangelo | Dynamic anatomy, contrapposto, muscular tension, heroic proportion (9 heads), Sistine Chapel ceiling — extreme foreshortening |
| Rembrandt | Chiaroscuro mastery, Rembrandt lighting (triangle on cheek), emotional faces through shadow, limited palette drama |
| Caravaggio | Tenebrism (extreme dark/light), theatrical staging, diagonal compositions, spotlight focus |
| Vermeer | Light through windows, color temperature control, intimate composition, optical precision |
| J.M.W. Turner | Atmospheric light, color as emotion, landscapes dissolving into abstraction |
| Alphonse Mucha | Art Nouveau line work, decorative framing, figure-as-ornament, flowing hair/fabric patterns |
| Hokusai | Ukiyo-e composition, Great Wave dynamic balance, nature dwarfing humans, bold flat color areas |
| Ivan Aivazovsky | Water and light mastery, sea as living entity, translucent waves, storm drama |
| Ilya Repin | Russian realism, group composition (Barge Haulers), emotional truth, historical narrative painting |
| Vasily Vereshchagin | War art without glorification (Apotheosis of War — skull pyramid), documentary honesty |
| Kazimir Malevich | Suprematism, shape-as-meaning, Black Square — pure form, geometric abstraction |

### Illustration & Comics
| Master | Key Techniques |
|--------|---------------|
| Moebius (Jean Giraud) | Line weight variation, vast sci-fi landscapes, intricate detail density, Arzach color palettes |
| Frank Frazetta | Dynamic figure painting, barbaric energy, warm-cool contrast, muscular anatomy in motion |
| Yoshitaka Amano | Ethereal watercolor style, flowing lines, fantasy elegance, Final Fantasy character design |
| Mike Mignola | Heavy shadow shapes, minimal detail maximum impact, Hellboy silhouette language, flat color + black |
| Akira Toriyama | Clean readable character design, action poses, Dragon Ball shape language, mechanical detail |
| Hayao Miyazaki | Environmental wonder, flight and movement, Studio Ghibli color warmth, lived-in worlds |
| Kim Jung Gi | Perspective mastery from imagination, no preliminary sketch, spatial understanding, crowd composition |
| Ashley Wood | Painterly abstraction, mech design, texture-as-mood, controlled chaos |
| Katsuya Terada | Ink mastery, monster design, dense organic detail, East-meets-West style fusion |
| Junji Ito | Horror through detail, spirals and distortion, uncanny valley faces, Uzumaki visual escalation |

### Game Art & Concept Design
| Artist/Studio | Key Techniques |
|---------------|---------------|
| Yoji Shinkawa (Metal Gear) | Ink wash character design, military mech aesthetics, brush stroke energy, silhouette-first design |
| Tetsuya Nomura (Final Fantasy) | Belt-and-zipper maximalism, character complexity, weapon-as-personality, anime-realism fusion |
| Hidetaka Miyazaki / FromSoft art team | Gothic architecture, oppressive scale, creature design from mythology, environmental dread |
| Fumito Ueda (ICO, Shadow of the Colossus) | Minimalist beauty, scale contrast (tiny hero vs colossus), muted palettes, melancholy light |
| Valve (Half-Life 2, Portal, TF2) | Industrial utilitarianism (HL2), clean sterile horror (Portal), stylized readable silhouettes (TF2) |
| CD Projekt Red (Witcher, Cyberpunk) | Slavic fantasy aesthetic, neon noir, lived-in world detail, culturally grounded design |
| Artyom Galeev / 4A Games (Metro) | Post-apocalyptic Russian aesthetic, underground claustrophobia, improvised technology, candlelight warmth in cold |
| GSC Game World (S.T.A.L.K.E.R.) | Chernobyl brutalism, Zone atmosphere, military surplus aesthetic, nature reclaiming civilization |
| Supergiant Games (Hades, Transistor) | Bold color blocking, character readability at small scale, UI-as-art, stylized anatomy |
| Playdead (Limbo, Inside) | Silhouette-only storytelling, monochrome mood, scale horror, minimal palette maximum atmosphere |
| Team Cherry (Hollow Knight) | Insect-inspired character design, hand-drawn charm, environmental mood through color shift |
| Studio MDHR (Cuphead) | 1930s rubber hose animation, hand-inked frames, watercolor backgrounds, vintage palette |

### Animation & Film
| Source | Key Techniques |
|--------|---------------|
| Studio Ghibli | Background painting (Kazuo Oga), natural color palettes, clouds and sky as emotional cue |
| Disney Renaissance | 12 principles of animation applied to still art: squash-stretch, anticipation, staging |
| Spider-Verse (2018) | Ben-Day dots, multi-style collision, frame rate as style choice, comic panel composition |
| Akira (1988) | Cyberpunk city detail, light trails, motorcycle red, explosion scale, Neo-Tokyo as character |
| Ghost in the Shell (1995) | Cyberpunk rain, Hong Kong density, digital-organic interface, reflective surfaces |
| Blade Runner (Scott/Villeneuve) | Neon in rain, brutalist mega-structures, orange-teal palette, fog-as-composition-tool |
| Mad Max: Fury Road | Desert palette exploded (orange sky, blue night), vehicle-as-character, kinetic composition |
| Wes Anderson | Symmetrical composition, pastel palettes, dollhouse framing, typography-as-design |
| Roger Deakins (cinematography) | Natural light mastery, silhouette staging, 1917 continuous frame, Blade Runner 2049 monochrome environments |
| Emmanuel Lubezki (cinematography) | Natural light only, long takes, wide-angle immersion, The Revenant survival atmosphere |

### Architecture & Environment Reference
| Source | Key Techniques |
|--------|---------------|
| Zaha Hadid | Fluid parametric forms, impossible-looking structures, futuristic organic architecture |
| Brutalism (Corbusier, Soviet) | Raw concrete, monumental scale, oppressive geometry, Metro/STALKER aesthetic origin |
| Art Deco (Chrysler Building, Rapture) | Geometric ornament, gold and chrome, Bioshock Rapture's design DNA |
| Wabi-sabi (Japanese) | Beauty in imperfection, aged materials, Ghost of Tsushima temple aesthetic |
| Soviet Constructivism | Propaganda poster composition, bold diagonals, red-black-white, Atomic Heart's visual DNA |
| Favela / Informal architecture | Organic growth, stacked structures, colorful chaos, Overwatch/Apex favela maps |

---

## Part 1: Anatomy & Proportion

### 1.1 Human Proportion Systems

#### Standard (Realistic) — 7.5 heads tall
```
HEAD    [1] — crown to chin
CHEST   [2] — chin to nipple line  
WAIST   [3] — nipple to navel
HIP     [4] — navel to crotch
THIGH   [5] — crotch to mid-thigh
KNEE    [6] — mid-thigh to below knee
SHIN    [7] — below knee to mid-shin
FOOT   [7.5] — mid-shin to sole
```
- Shoulders = 2-2.5 head widths (male), 1.5-2 (female)
- Arms reach mid-thigh when relaxed
- Elbow aligns with waist/navel
- Hands = face length (chin to hairline)
- Foot = forearm length (wrist to elbow)
- *Used in*: Realistic game art, CD Projekt Red, Naughty Dog

#### Heroic — 8-9 heads tall (Michelangelo)
- Longer legs, broader shoulders
- More dramatic, idealized
- *Used in*: FromSoft, Metal Gear, superhero games, Frazetta paintings

#### Stylized — 3-6 heads tall
- **Chibi (2-3 heads)**: Cute, expressive, Hollow Knight
- **Semi-deformed (4-5 heads)**: Hades, Genshin Impact, most anime games
- **Semi-realistic (6 heads)**: Team Fortress 2, Overwatch, Fortnite
- *Rule*: Head size grows = character feels younger/cuter. Head size shrinks = more serious/mature.

### 1.2 Contrapposto & Weight

A standing figure must show WHERE their weight rests:
- **Contrapposto**: Weight on one leg, opposite shoulder drops, hip shifts — creates S-curve
- *Invented by*: Ancient Greeks, perfected by Michelangelo (David)
- **Rule**: If both feet are flat and shoulders level, the figure looks like a mannequin, not a person
- Weight distribution tells story: confident (centered), exhausted (leaning), nervous (shifting)

### 1.3 Gesture & Line of Action

Before any detail, draw ONE line that captures the pose's energy:
- **C-curve**: Relaxed, elegant, flowing (Mucha figures)
- **S-curve**: Dynamic, contrapposto, feminine (Botticelli Venus)
- **Diagonal**: Action, falling, lunging (Frazetta warriors)
- **Vertical**: Authority, stillness, power (military portraits)
- **Broken/angular**: Tension, pain, fear (Junji Ito horror)

**Rule**: If the gesture line is boring, no amount of detail saves the pose.

### 1.4 Foreshortening

Objects closer to camera appear larger. Critical for dynamic poses:
- Fist punching toward viewer = huge fist, small body
- *Master class*: Michelangelo (Sistine Chapel), Kim Jung Gi (extreme angles from imagination)
- In SVG: Use scale transforms + overlap to imply depth
- **Rule**: When in doubt, make the foreshortening MORE extreme, not less. Timid foreshortening looks wrong.

### 1.5 Face Proportions

Standard face division:
```
HAIRLINE ──────── top quarter
EYEBROW  ──────── eyes sit at vertical center
NOSE     ──────── bottom of nose at 3/4 mark
MOUTH    ──────── 1/3 between nose and chin
CHIN     ──────── bottom
```
- Eyes are ONE eye-width apart
- Mouth width = between pupils
- Ears: top at eyebrow, bottom at nose
- *Stylization*: Bigger eyes = younger/anime. Smaller eyes = realistic/gritty. Eye placement is the single biggest factor in character "feel."

---

## Part 2: Composition

### 2.1 The Golden Ratio (φ = 1.618)

Divide the canvas by φ to find natural focal points:
```
┌─────────────┬────────┐
│             │        │
│      A      │   B    │
│             │        │
├─────────────┤        │
│      C      │   D    │
└─────────────┴────────┘
  A:B = φ      C:D = φ
```
- Place primary subject at golden ratio intersection points
- Works fractally — apply within sub-sections too
- *Used by*: Da Vinci (Mona Lisa, Last Supper), Vermeer, most Ghibli backgrounds
- **Rule**: The eye naturally rests at φ points. Fight this only intentionally.

### 2.2 Golden Spiral

Fibonacci spiral guiding eye movement through the image:
```
┌───────────────────┬──────────┐
│                   │    ┌──┐  │
│                   │    │╭─┘  │
│                   │    ╰─┘   │
│                   │          │
│                   ├────┬─────┤
│                   │    │     │
└───────────────────┴────┴─────┘
```
- Eye follows the spiral from largest area to focal point
- Place most important element at spiral center
- *Master class*: Hokusai (Great Wave — wave curl IS the spiral)

### 2.3 Rule of Thirds

Simpler than golden ratio, sufficient for most game art:
```
┌─────┬─────┬─────┐
│     │     │     │
│  ●  │     │  ●  │  ← power points
├─────┼─────┼─────┤
│     │     │     │
│  ●  │     │  ●  │  ← power points
├─────┼─────┼─────┤
│     │     │     │
└─────┴─────┴─────┘
```
- Subject on vertical third line, NOT center (unless symmetry is intentional — Wes Anderson)
- Horizon on horizontal third (upper = grounded feel, lower = sky/freedom feel)
- *Used everywhere*: Screenshots, UI layout, level design sight lines

### 2.4 Leading Lines

Lines in the image that guide the eye toward the focal point:
- Roads, rivers, fences, weapon barrels, eye direction, light beams
- **Converging lines** = depth (train tracks vanishing)
- **Parallel lines** = stability (columns, Brutalist buildings)
- **Diagonal lines** = tension, action, instability (Caravaggio, Soviet Constructivist posters)
- **Curved lines** = organic, elegant, flowing (Mucha, Ghibli)

### 2.5 Framing & Negative Space

- **Frame within frame**: Doorways, windows, arches drawing attention inward (Vermeer, FromSoft architecture)
- **Negative space**: Empty area that gives the subject room to "breathe"
  - Lots of negative space = isolation, loneliness (Shadow of the Colossus, Limbo)
  - No negative space = claustrophobia, density (Akira, Metro)
- **Figure-ground relationship**: Subject must separate from background. Use value contrast, not just color.

### 2.6 Symmetry & Asymmetry

- **Symmetry**: Power, authority, divinity, order (throne rooms, temples, Wes Anderson)
- **Asymmetry**: Life, movement, narrative tension, natural world
- **Broken symmetry**: Order disrupted — strongest storytelling tool (symmetrical building with one wall collapsed)

### 2.7 Tangents (Anti-Pattern)

**Tangent**: When two edges barely touch or align, creating visual confusion.
- Character's head touching the horizon line = head looks "stuck" to it
- Two objects' edges meeting = they look merged
- **Fix**: Clearly overlap OR clearly separate. Never "just touch."

---

## Part 3: Color Theory

### 3.1 The Color Wheel

```
           RED
        /      \
   ORANGE      MAGENTA
      |           |
  YELLOW       VIOLET
      \         /
        \     /
         GREEN
```

#### Color Relationships
| Scheme | Description | Mood | Example |
|--------|------------|------|---------|
| Complementary | Opposite on wheel (red-green, blue-orange) | High contrast, vibrant, tense | Blade Runner (orange-teal) |
| Analogous | Neighbors on wheel (blue-teal-green) | Harmonious, calm, natural | Ghibli forest scenes |
| Triadic | 3 equidistant colors | Playful, balanced, energetic | Spider-Verse, Cuphead |
| Split complementary | Main + two neighbors of complement | Vibrant but less tense | Hades (red, gold, teal) |
| Monochromatic | One hue, varying saturation/value | Unified, atmospheric, dramatic | Limbo, Inside, Playdead |

### 3.2 Color Temperature

- **Warm** (red, orange, yellow): Energy, danger, passion, comfort (firelight)
- **Cool** (blue, green, violet): Calm, sadness, mystery, technology
- **Temperature contrast** is more powerful than hue contrast
- **Rule**: Light and shadow have opposite temperature. If light is warm (sun), shadows are cool (blue). If light is cool (moonlight), shadows are warm (amber).
- *Master class*: Rembrandt (warm candlelight, cool background), Vermeer (cool window light, warm skin)

### 3.3 Value (Light/Dark)

Value > Color. A piece that works in grayscale will work in color. Not vice versa.

**Value structure (5-value system):**
```
█████ — 100% — Black (deepest shadow)
▓▓▓▓▓ —  75% — Dark (shadow)
▒▒▒▒▒ —  50% — Mid (transition)
░░░░░ —  25% — Light (lit area)
      —   0% — White (highlight)
```

- **High key** (mostly light values): Dreamy, ethereal, innocent (Ghibli clouds)
- **Low key** (mostly dark values): Dramatic, dangerous, noir (Caravaggio, Metro)
- **Full range**: Dynamic, realistic (most game art)
- **Rule**: Squint at your image. If you can't read the shapes, your values are wrong.

### 3.4 Saturation

- **High saturation**: Cartoon, energetic, overwhelming (Cuphead, Jet Set Radio)
- **Low saturation**: Realistic, muted, melancholy (Limbo, This War of Mine)
- **Selective saturation**: Mostly muted with ONE saturated element = instant focal point
  - *Used in*: Schindler's List (red coat), Sin City, our radar officer concept (red scarf)
- **Rule**: Desaturate the background, saturate the subject. The eye goes to color.

### 3.5 Color Psychology in Games

| Color | Association | Game Use |
|-------|-----------|----------|
| Red | Danger, health, passion, aggression | Health bars, enemy indicators, critical items |
| Blue | Technology, calm, cold, sadness | Shields, mana, UI elements, water |
| Green | Nature, health, safety, poison | Health pickups, safe zones, also: poison/acid (context!) |
| Yellow | Warning, treasure, energy, optimism | Loot glow, quest markers, caution |
| Orange | Warmth, fire, urgency, community | Campfires (safe), explosions (danger) — dual nature |
| Purple | Magic, mystery, corruption, royalty | Arcane effects, rare items, void/corruption |
| White | Purity, death, emptiness, divine | Snow, spirits, blank spaces, holy damage |
| Black | Death, unknown, power, elegance | Shadows, void, boss arenas, stealth |

### 3.6 Palette Construction

For any game art piece, define:
1. **Dominant** (60%): Sets the overall mood
2. **Secondary** (30%): Supports and contrasts
3. **Accent** (10%): Draws the eye, pops

**Example palettes by mood:**
- **War/military**: Olive + Dust/khaki + Blood red accent
- **Cyberpunk**: Deep blue + Neon magenta + Teal accent
- **Fantasy forest**: Deep green + Gold + Violet accent
- **Horror**: Near-black + Desaturated blue + Sickly yellow accent
- **Soviet retro-future**: Concrete gray + Propaganda red + Gold accent

---

## Part 4: Light & Shadow

### 4.1 Light Direction & Mood

| Direction | Mood | Use |
|-----------|------|-----|
| **Top-front (45°)** | Natural, neutral, readable | Standard game art, character sheets |
| **Side (90°)** | Dramatic, split personality, conflict | Half-lit faces, noir, Two-Face moments |
| **Below (uplighting)** | Horror, supernatural, villain reveal | Campfire horror stories, boss reveals |
| **Behind (rim/backlight)** | Heroic, mysterious, silhouette | Hero entrances, dramatic reveals, Frazetta |
| **Above (top-down)** | Oppressive, divine, interrogation | Overhead sun in desert, spotlight scenes |
| **Ambient (no clear source)** | Flat, dreamlike, stylized | UI art, icons, Cuphead, TF2 |

### 4.2 Lighting Setups

#### Rembrandt Lighting
- Light from 45° above and to one side
- Creates triangle of light on shadowed cheek
- *The* portrait lighting. If unsure, use this.
- *Master*: Rembrandt van Rijn

#### Chiaroscuro
- Extreme contrast between light and dark
- Most of the image is in shadow; light sculpts the subject
- *Masters*: Caravaggio, Rembrandt
- *Game use*: Metro candlelight scenes, Dark Souls bonfires

#### Rim Lighting (Contre-jour)
- Light source behind subject, creating bright edge/halo
- Subject is mostly silhouette
- *Used in*: Hero shots, Frazetta barbarians, Boss introductions

#### Ambient Occlusion
- Soft shadows in crevices where surfaces meet
- Adds depth and "grounding" to flat art
- *Where*: Where wall meets floor, under chin, inside folds of clothing
- In SVG: Use subtle dark gradients at junction points

### 4.3 Cast Shadows

Shadows tell you:
- **Time of day** (long = dawn/dusk, short = noon)
- **Light source** (direction and distance)
- **Surface shape** (shadow follows terrain)
- **Rule**: Cast shadows are harder-edged close to the object, softer further away

### 4.4 Reflected Light

Light bounces off surfaces and fills shadows:
- Red floor reflects red into shadows above
- Blue sky reflects cool light into outdoor shadows
- **Rule**: Shadows are never pure black. They contain reflected light of the environment's color.
- *Master class*: Vermeer (cool reflections from white walls), Aivazovsky (green sea reflecting into clouds)

---

## Part 5: Perspective

### 5.1 One-Point Perspective

One vanishing point on horizon. Viewer looks "straight ahead."
```
         ╲    |    ╱
          ╲   |   ╱
           ╲  |  ╱
            ╲ | ╱
             ╲|╱
         ─────●───── horizon
             ╱|╲
            ╱ | ╲
```
- *Used for*: Corridors, roads, tunnels, symmetric views
- *Master class*: Da Vinci (Last Supper — VP at Christ's head), Metro tunnels

### 5.2 Two-Point Perspective

Two VPs on horizon. Viewer looks at a corner.
```
           ╱  |  ╲
          ╱   |   ╲
     ────●────|────●──── horizon
          ╲   |   ╱
           ╲  |  ╱
```
- *Used for*: Most building exteriors, street scenes, environments
- *Most common* perspective in game concept art

### 5.3 Three-Point Perspective

Two VPs on horizon + one above or below. Viewer looks up or down.
- VP above = looking up at a skyscraper (power, awe)
- VP below = looking down from height (vertigo, control)
- *Used for*: Dramatic establishing shots, cyberpunk cityscapes, boss scale
- *Master class*: Kim Jung Gi (extreme 3-point from imagination)

### 5.4 Atmospheric (Aerial) Perspective

Distant objects become:
- **Lighter** in value
- **Cooler** in temperature (shift toward blue)
- **Less saturated**
- **Less detailed** (edges soften)

*This is the #1 technique for creating depth in 2D art without literal perspective lines.*
- *Masters*: Da Vinci (Mona Lisa background), Turner, Aivazovsky, every Ghibli landscape
- In SVG: Layer objects with decreasing opacity and blue shift

### 5.5 Scale & Depth Cues

When perspective lines aren't enough:
| Cue | Technique |
|-----|-----------|
| **Overlap** | Near objects cover far objects (strongest depth cue) |
| **Size gradient** | Same objects getting smaller = distance |
| **Detail gradient** | More detail near, less detail far |
| **Value gradient** | Darker near, lighter far (atmospheric) |
| **Texture gradient** | Visible texture near, smooth far |
| **Position** | Lower on canvas = closer (ground plane) |

---

## Part 6: Silhouette & Shape Language

### 6.1 The Silhouette Test

Fill your character pure black. Can you still tell:
- Who they are?
- What they do?
- Their mood/personality?

If no → redesign. Silhouette readability is NON-NEGOTIABLE.
- *Master class*: TF2 (every class instantly readable), Hollow Knight, Mignola's Hellboy

### 6.2 Shape Language

Shapes communicate subconsciously:

| Shape | Feeling | Character Type | Example |
|-------|---------|---------------|---------|
| **Circle / Round** | Friendly, soft, approachable, innocent | Sidekicks, children, healers | Baymax, Kirby, BB-8 |
| **Square / Block** | Stable, strong, reliable, stubborn | Tanks, protectors, soldiers | Hellboy, Heavy (TF2) |
| **Triangle / Angular** | Dangerous, aggressive, fast, cunning | Villains, assassins, predators | Maleficent, Pyramid Head |
| **Mixed round+square** | Trustworthy but strong | Heroes, protagonists | Mario, Link |
| **Mixed triangle+round** | Dangerous but attractive | Anti-heroes, femme fatales | Bayonetta, Widowmaker |

**Rule**: Start design with basic shapes. If the shapes don't communicate the character, details won't save it.

### 6.3 Design Hierarchy

Every character design needs:
1. **Primary read** (silhouette): Recognizable at thumbnail size — shape, proportion, posture
2. **Secondary read** (mid-distance): Color, major details — armor type, weapon, clothing style
3. **Tertiary read** (close-up): Fine details — buckles, insignia, scars, stitching

*Design for primary first. Most players see characters at secondary distance. Tertiary is for fan art and cutscenes.*

---

## Part 7: Style & Art Direction

### 7.1 Style Spectrum

```
ABSTRACT ←──────────────────────────────────→ PHOTOREALISTIC
  Limbo    Cuphead    Hades    Witcher 3    TLOU2
  Malevich  Mucha     Amano    Shinkawa     Repin
```

Choosing where on the spectrum:
- **Abstract**: Mood over accuracy, strong shape language, Playdead, Limbo
- **Stylized**: Exaggerated features, readable, Hades, Cuphead, Ghibli
- **Semi-realistic**: Grounded but heightened, most AAA concept art
- **Photorealistic**: Maximum detail, only for final production, not concept phase

### 7.2 Visual Consistency Rules

Within a single project, maintain:
- **Line weight**: Consistent thickness or intentional variation pattern
- **Edge treatment**: Hard edges everywhere (Mignola) OR soft edges (Amano) OR mixed with rules
- **Color range**: Locked palette, max 5-6 base hues
- **Detail density**: Uniform detail level or intentional contrast (detailed character, simple background)
- **Shape language family**: Characters in the same world should share shape DNA

### 7.3 Cultural Visual DNA

| Setting | Visual DNA Source | Key Elements |
|---------|------------------|-------------|
| Russian/Soviet | Constructivism, Socialist Realism, brutalist architecture | Bold reds, propaganda composition, concrete textures, heroic figures |
| Japanese | Ukiyo-e, wabi-sabi, anime, karesansui | Clean lines, negative space, cherry blossom pink, asymmetric balance |
| Cyberpunk | Blade Runner, Akira, Ghost in the Shell | Neon in darkness, rain reflections, vertical cities, tech-organic fusion |
| Dark Fantasy | FromSoft, Berserk, Gothic architecture | Oppressive scale, organic horror, cathedral geometry, muted palettes |
| Post-apocalyptic | Metro, STALKER, Mad Max | Decay textures, improvised tech, nature reclaiming, warm fires in cold ruins |
| Retro-futurism | Atomic Heart, Fallout, Bioshock | Art Deco + atomic age, chrome and vacuum tubes, optimistic decay |
| Military/Modern | Broken Arrow, ARMA, Ghost Recon | Tactical gear detail, camo patterns, vehicle silhouettes, dust and grit |

---

## Part 8: SVG & HTML Technique Guide

### 8.1 SVG Best Practices for Art

- **Gradients**: Use radial gradients for organic forms, linear for architecture
- **Filters**: `feGaussianBlur` for atmospheric perspective, `feDropShadow` for depth
- **Clip paths**: For complex overlapping shapes
- **Opacity layers**: Stack semi-transparent shapes for painterly effect
- **Group organization**: `<g>` tags by layer (background, midground, foreground, character, annotations)
- **Viewport**: Minimum 1200x900 for concept art, 800x600 for icons/symbols
- **Transform**: Use `scale()` and `translate()` for depth composition

### 8.2 Creating Depth in SVG

1. **Background layer**: Lightest values, coolest colors, most blur, least detail
2. **Midground layer**: Medium values, medium detail
3. **Foreground layer**: Darkest darks AND brightest lights, warmest colors, most detail
4. **Atmospheric haze**: Semi-transparent rectangle with background color between layers

### 8.3 HTML/Canvas for Interactive Art

- Use for: Level layout prototypes, UI mockups, interactive maps
- CSS custom properties for theming: `--color-primary`, `--color-accent`
- Canvas API for complex procedural art (terrain, particles, lighting effects)
- Self-contained single HTML file, no external dependencies

---

## Part 9: Anti-Patterns

| Anti-Pattern | Problem | Fix |
|-------------|---------|-----|
| **Pillow shading** | Light from everywhere = flat, no depth | Choose ONE dominant light direction |
| **Tangent lines** | Edges touching = visual confusion | Overlap clearly OR separate clearly |
| **Same-face syndrome** | All characters have identical face structure | Vary face shapes: round, angular, long, wide |
| **Detail everywhere** | No focal point, eye wanders | Detail the focal point, simplify the rest |
| **Noodle arms** | Limbs without bone/muscle structure | Study anatomy: joints, muscle groups, weight |
| **Floating figures** | Characters don't touch the ground convincingly | Cast shadow, feet perspective, ground contact |
| **Rainbow palette** | Too many saturated colors competing | Limit to 3-4 hues, vary through saturation/value |
| **Symmetric characters** | Unnaturally balanced, lifeless | Break symmetry: weight shift, different hands, asymmetric gear |
| **Generic armor** | Plate armor with no cultural/functional identity | Research real armor, add faction identity, show wear |
| **Copy-paste crowds** | Repeated identical figures | Vary silhouettes, colors, poses, even in background crowds |

---

## Part 10: Practical Workflows

### 10.1 Character Concept Workflow

1. **Silhouette thumbnails** (5-10 variations, black fill only)
2. **Select strongest silhouette** — must pass the "who/what/mood" test
3. **Basic shapes** over silhouette — define major forms
4. **Proportion check** — count heads, check landmark alignments
5. **Value pass** — grayscale rendering, establish light direction
6. **Color pass** — apply palette, temperature contrast
7. **Detail pass** — add tertiary details, textures, insignia
8. **Environment context** — even a simple background grounds the character

### 10.2 Environment Concept Workflow

1. **Composition sketch** — thumbnail with value blocks only
2. **Perspective setup** — place horizon and vanishing points
3. **Value structure** — 3-5 values maximum for initial pass
4. **Atmospheric depth** — apply aerial perspective to layers
5. **Color mood** — apply palette, warm/cool distribution
6. **Focal point detail** — render only the area of interest
7. **Storytelling elements** — add narrative micro-details

### 10.3 Image Generation (Pollinations.ai)

For high-quality concept art, use the built-in image generator (free, no API key):

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/generate_image.py generate "<prompt>" <output_path> [width] [height] [model]
```

**Models:** `flux` (default, best), `flux-realism`, `flux-anime`, `flux-3d`, `flux-pixel`, `turbo`

**When to use what:**
- **Image generation** → characters, environments, mood boards, key art, anything requiring photorealism or painterly quality
- **SVG** → maps, UI mockups, diagrams, faction symbols, level layouts, anything requiring editability

**Prompt engineering:** Apply ALL methodology from Parts 1-9 to write the prompt. A good prompt includes:
subject + pose/anatomy + clothing + environment + lighting setup + color palette + style reference + mood + composition + quality tags.

### 10.4 Using Agents

This plugin provides specialized agents for different visual tasks:

- **visual-artist** — general purpose 2D art creation (characters, environments, items) using image generation or SVG
- **style-director** — establishes and maintains visual style guides for projects
- **anatomy-checker** — reviews existing art for proportion and anatomy issues
