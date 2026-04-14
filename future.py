"""
╔══════════════════════════════════════════════════════════════╗
║        AI FUUTURE YOU — future.py               ║
║        Behavior-to-Future Modeling System                    ║
║        Built with Streamlit | 100% Free | No API Keys       ║
╚══════════════════════════════════════════════════════════════╝
"""

import streamlit as st
import math

# ─────────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="FUTURE YOU",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────────────────────
# CUSTOM CSS — Dark futuristic theme
# ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;600&display=swap');

  /* Global */
  html, body, [class*="css"] {
    font-family: 'Rajdhani', sans-serif;
    background-color: #0a0a0f;
    color: #e0e0f0;
  }

  /* Hide Streamlit branding */
  #MainMenu {visibility: hidden;}
  footer {visibility: hidden;}
  header {visibility: hidden;}

  /* Main container */
  .block-container {
    padding-top: 3rem;
    padding-bottom: 3rem;
    max-width: 900px;
}

  /* Hero title */
  .hero-title {
    font-family: 'Orbitron', monospace;
    font-size: 2.6rem;
    font-weight: 900;
    background: linear-gradient(135deg, #00f5ff, #7b2fff, #ff006e);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-align: center;
    letter-spacing: 2px;
    margin-bottom: 0.2rem;
  }

  .hero-sub {
    text-align: center;
    color: #8888aa;
    font-size: 1.1rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 2rem;
  }

  /* Section headers */
  .section-header {
    font-family: 'Orbitron', monospace;
    font-size: 1rem;
    color: #00f5ff;
    letter-spacing: 3px;
    text-transform: uppercase;
    border-bottom: 1px solid #1a1a3a;
    padding-bottom: 8px;
    margin-bottom: 1.2rem;
    margin-top: 1.5rem;
  }

  /* Scenario cards */
  .card-current {
    background: linear-gradient(135deg, #0f1529 0%, #0a0f20 100%);
    border: 1px solid #1e3a5f;
    border-left: 4px solid #00f5ff;
    border-radius: 12px;
    padding: 1.4rem;
    margin-bottom: 1rem;
  }

  .card-best {
    background: linear-gradient(135deg, #0a1f0a 0%, #051205 100%);
    border: 1px solid #1e5f2a;
    border-left: 4px solid #39ff14;
    border-radius: 12px;
    padding: 1.4rem;
    margin-bottom: 1rem;
  }

  .card-worst {
    background: linear-gradient(135deg, #1f0a0a 0%, #120505 100%);
    border: 1px solid #5f1e1e;
    border-left: 4px solid #ff003c;
    border-radius: 12px;
    padding: 1.4rem;
    margin-bottom: 1rem;
  }

  /* Card titles */
  .card-title-current {
    font-family: 'Orbitron', monospace;
    font-size: 0.85rem;
    color: #00f5ff;
    letter-spacing: 2px;
    margin-bottom: 0.8rem;
  }

  .card-title-best {
    font-family: 'Orbitron', monospace;
    font-size: 0.85rem;
    color: #39ff14;
    letter-spacing: 2px;
    margin-bottom: 0.8rem;
  }

  .card-title-worst {
    font-family: 'Orbitron', monospace;
    font-size: 0.85rem;
    color: #ff003c;
    letter-spacing: 2px;
    margin-bottom: 0.8rem;
  }

  /* Score labels */
  .score-label {
    font-size: 0.78rem;
    color: #9999bb;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 2px;
  }

  .score-value {
    font-family: 'Orbitron', monospace;
    font-size: 1.3rem;
    font-weight: 700;
    margin-bottom: 4px;
  }

  /* Story text */
  .story-text {
    font-size: 0.92rem;
    color: #bbbbcc;
    line-height: 1.7;
    font-style: italic;
    border-left: 2px solid #333;
    padding-left: 12px;
    margin-top: 0.8rem;
  }

  /* Overall score badge */
  .overall-badge {
    font-family: 'Orbitron', monospace;
    font-size: 2.2rem;
    font-weight: 900;
    text-align: center;
  }

  /* Input section */
  .input-box {
    background: #0e0e1e;
    border: 1px solid #1a1a35;
    border-radius: 12px;
    padding: 1.5rem;
  }

  /* Slider labels */
  .stSlider > div > div > div > div {
    background: linear-gradient(90deg, #7b2fff, #00f5ff) !important;
  }

  /* Progress bars */
  .stProgress > div > div > div > div {
    background: linear-gradient(90deg, #7b2fff, #00f5ff);
  }

  /* Divider */
  hr {
    border-color: #1a1a3a;
    margin: 1.5rem 0;
  }

  /* Tooltip / info box */
  .info-pill {
    display: inline-block;
    background: #1a1a3a;
    color: #7777aa;
    border-radius: 20px;
    padding: 3px 12px;
    font-size: 0.75rem;
    letter-spacing: 1px;
    margin-right: 6px;
  }

  /* Age tag */
  .age-tag {
    font-family: 'Orbitron', monospace;
    font-size: 0.7rem;
    color: #555577;
    margin-bottom: 0.4rem;
    letter-spacing: 2px;
  }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# SCORING ENGINE (Deterministic — same input = same output)
# ─────────────────────────────────────────────────────────────

def clamp(value, min_val=0, max_val=100):
    """Keeps a value strictly between min and max."""
    return max(min_val, min(max_val, value))

def calculate_scores(sleep, study, screen, exercise, social, spending):
    """
    Rule-based scoring system.
    Each score is calculated from weighted input factors.
    All formulas are deterministic (no randomness).
    """

    # ── HEALTH SCORE ──────────────────────────────────────────
    # Ideal sleep = 7–8 hrs. Penalty for too little or too much.
    sleep_score   = 100 - abs(sleep - 7.5) * 12        # peaks at 7.5h
    screen_pen    = screen * 5                           # each hr screen = -5
    exercise_bon  = exercise * 18                        # each hr exercise = +18
    health = clamp(sleep_score - screen_pen + exercise_bon)

    # ── CAREER SCORE ──────────────────────────────────────────
    # Study/work is the main driver; sleep deprivation hurts focus
    study_score   = study * 7.5                          # 0–90 from study
    sleep_focus   = -max(0, (7 - sleep)) * 8            # penalty if <7h sleep
    screen_dist   = -screen * 3                          # distraction penalty
    career = clamp(study_score + sleep_focus + screen_dist + 10)

    # ── WEALTH SCORE ──────────────────────────────────────────
    spending_map  = {"Low": 30, "Medium": 0, "High": -30}
    spending_val  = spending_map[spending]
    career_bonus  = career * 0.3                         # career drives wealth
    wealth = clamp(50 + spending_val + career_bonus - screen * 2)

    # ── HAPPINESS SCORE ───────────────────────────────────────
    social_bon    = social * 10                          # social = +10/hr
    exercise_hap  = exercise * 12                        # endorphins!
    screen_hap    = -screen * 6                          # doom-scrolling kills joy
    sleep_hap     = -max(0, (7 - sleep)) * 7            # bad sleep = sad
    happiness = clamp(40 + social_bon + exercise_hap + screen_hap + sleep_hap)

    return {
        "health":    round(health),
        "career":    round(career),
        "wealth":    round(wealth),
        "happiness": round(happiness),
        "overall":   round((health + career + wealth + happiness) / 4),
    }

def make_improved(sleep, study, screen, exercise, social, spending):
    """Generate 'Best Case' by nudging habits positively."""
    spend_upgrade = {"Low": "Low", "Medium": "Low", "High": "Medium"}
    return (
        min(sleep + 1.0, 8.5),
        min(study + 1.5, 12),
        max(screen - 1.5, 0),
        min(exercise + 0.5, 3),
        min(social + 0.5, 5),
        spend_upgrade[spending],
    )

def make_worst(sleep, study, screen, exercise, social, spending):
    """Generate 'Worst Case' by nudging habits negatively."""
    spend_downgrade = {"Low": "Medium", "Medium": "High", "High": "High"}
    return (
        max(sleep - 1.5, 0),
        max(study - 1.5, 0),
        min(screen + 2.0, 12),
        max(exercise - 0.5, 0),
        max(social - 1.0, 0),
        spend_downgrade[spending],
    )


# ─────────────────────────────────────────────────────────────
# STORY GENERATOR (Template-based, no API needed)
# ─────────────────────────────────────────────────────────────

def generate_story(scores, scenario_type, sleep, study, screen, exercise, social, spending):
    """Generates a dynamic story paragraph based on scores and habits."""

    overall = scores["overall"]
    health  = scores["health"]
    career  = scores["career"]
    wealth  = scores["wealth"]
    happy   = scores["happiness"]

    # Pick career tier
    if career >= 75:
        career_line = "killing it in your career — promotions feel like a habit"
    elif career >= 50:
        career_line = "doing decently at work, though you know you could push harder"
    elif career >= 30:
        career_line = "struggling to keep up professionally, stuck in a loop of burnout"
    else:
        career_line = "in a serious career slump — consistency is nowhere to be found"

    # Pick health tier
    if health >= 75:
        health_line = "physically thriving — people literally ask for your routine"
    elif health >= 50:
        health_line = "holding it together health-wise, but energy dips are real"
    elif health >= 30:
        health_line = "running on fumes — your body is sending SOS signals daily"
    else:
        health_line = "in a rough health spot — small tasks feel like marathons"

    # Pick wealth tier
    if wealth >= 75:
        wealth_line = "your savings account is actually making you smile"
    elif wealth >= 50:
        wealth_line = "managing money okay — not rich, not broke, just... vibing"
    elif wealth >= 30:
        wealth_line = "financially stressed — impulse spending keeps setting you back"
    else:
        wealth_line = "in a tight spot financially — debt is a real convo you're avoiding"

    # Pick happiness tier
    if happy >= 75:
        happy_line = "genuinely content — your friends call you 'the vibe'"
    elif happy >= 50:
        happy_line = "mostly okay mentally, with occasional low-key existential dread"
    elif happy >= 30:
        happy_line = "dealing with regular stress and feeling chronically drained"
    else:
        happy_line = "struggling emotionally — burnout has entered the chat 😶"

    # Scenario-specific intro
    intros = {
        "current": "No cap —",
        "best":    "Glow-up arc unlocked 🔥 —",
        "worst":   "Yikes, real talk —",
    }
    intro = intros.get(scenario_type, "Basically —")

    # Overall verdict
    if overall >= 75:
        verdict = "Overall? You're living your best life, fr fr."
    elif overall >= 55:
        verdict = "Could be worse, could be better — mid arc, but improvable."
    elif overall >= 35:
        verdict = "You're surviving, not thriving. Time to audit those habits, bestie."
    else:
        verdict = "This timeline is giving 'cautionary tale' energy. Change is needed NOW."

    if scenario_type == "current":
        story = f"""
        This is you rn 👇

        💼 {career_line}  
        ❤️ {health_line}  
        💰 {wealth_line}  
        🧠 {happy_line}  

        Overall vibe: {verdict}
        """

    elif scenario_type == "best":
        story = f"""
        This version of you is kinda cracked 🚀

        💼 {career_line}  
        ❤️ {health_line}  
        💰 {wealth_line}  
        🧠 {happy_line}  

        You actually got your life together here.
        """

    else:  # worst
        story = f"""
        Yeah… this path ain’t it 💀

        💼 {career_line}  
        ❤️ {health_line}  
        💰 {wealth_line}  
        🧠 {happy_line}  

        You might wanna fix your habits fr.
        """
    return story


# ─────────────────────────────────────────────────────────────
# SCORE COLOR (for styling dynamic values)
# ─────────────────────────────────────────────────────────────

def score_color(val):
    if val >= 70:
        return "#39ff14"   # green
    elif val >= 45:
        return "#f5c518"   # yellow
    else:
        return "#ff003c"   # red

def score_emoji(val):
    if val >= 70:
        return "🟢"
    elif val >= 45:
        return "🟡"
    else:
        return "🔴"


# ─────────────────────────────────────────────────────────────
# RENDER SCENARIO CARD
# ─────────────────────────────────────────────────────────────

def render_scenario(label, card_class, title_class, scores, story, habit_summary):
    st.markdown(f'<div class="{card_class}">', unsafe_allow_html=True)
    st.markdown(f'<div class="{title_class}">◈ {label}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="age-tag">PROJECTED AGE 35 · {habit_summary}</div>', unsafe_allow_html=True)

    # Score rows
    cols = st.columns(4)
    icons = {"health": "❤️", "career": "💼", "wealth": "💰", "happiness": "😊"}
    labels = {"health": "HEALTH", "career": "CAREER", "wealth": "WEALTH", "happiness": "HAPPINESS"}

    for i, key in enumerate(["health", "career", "wealth", "happiness"]):
        val = scores[key]
        color = score_color(val)
        with cols[i]:
            st.markdown(f'<div class="score-label">{icons[key]} {labels[key]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="score-value" style="color:{color}">{val}</div>', unsafe_allow_html=True)
            st.progress(val / 100)

    # Overall
    overall = scores["overall"]
    color = score_color(overall)
    st.markdown(f"""
    <div style="text-align:right; margin-top:0.5rem;">
        <span style="font-size:0.75rem; color:#666688; letter-spacing:2px;">OVERALL SCORE </span>
        <span style="font-family:'Orbitron',monospace; font-size:1.6rem; font-weight:900; color:{color};">{overall}</span>
        <span style="font-size:0.75rem; color:#666688;">/100</span>
    </div>
    """, unsafe_allow_html=True)

    # Story
    st.markdown(f'<div class="story-text">{story}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# BAR CHART using Streamlit native
# ─────────────────────────────────────────────────────────────

def render_comparison_chart(scores_c, scores_b, scores_w):
    """Simple bar chart comparison using streamlit's built-in chart."""
    import pandas as pd

    data = {
        "Metric":     ["Health", "Career", "Wealth", "Happiness", "Overall"],
        "Current":    [scores_c["health"], scores_c["career"], scores_c["wealth"], scores_c["happiness"], scores_c["overall"]],
        "Best Case":  [scores_b["health"], scores_b["career"], scores_b["wealth"], scores_b["happiness"], scores_b["overall"]],
        "Worst Case": [scores_w["health"], scores_w["career"], scores_w["wealth"], scores_w["happiness"], scores_w["overall"]],
    }
    df = pd.DataFrame(data).set_index("Metric")
    st.bar_chart(df, color=["#00f5ff", "#39ff14", "#ff003c"], height=320)


# ─────────────────────────────────────────────────────────────
# RADAR CHART using matplotlib
# ─────────────────────────────────────────────────────────────
def generate_life_timeline(scores_c, scores_b, scores_w):
    import pandas as pd

    ages = list(range(20, 41, 2))  # 20 → 40

    def simulate_growth(base_score, growth_rate):
        values = []
        current = base_score

        for i in range(len(ages)):
            current = current + (growth_rate * (1 + i * 0.15))  # increasing effect
            current = max(0, min(100, current))
            values.append(current)

        return values

    current_path = simulate_growth(scores_c["overall"], 0.8)
    best_path    = simulate_growth(scores_b["overall"], 2.2)
    worst_path   = simulate_growth(scores_w["overall"], -2.0)

    df = pd.DataFrame({
        "Age": ages,
        "Current Path": current_path,
        "Best Path": best_path,
        "Worst Path": worst_path
    })

    df = df.set_index("Age")
    return df


def render_radar(scores_c, scores_b, scores_w):
    """Radar chart for visual WOW factor."""
    try:
        import matplotlib.pyplot as plt
        import matplotlib.patches as mpatches
        import numpy as np

        categories = ['Health', 'Career', 'Wealth', 'Happiness']
        N = len(categories)
        angles = [n / float(N) * 2 * math.pi for n in range(N)]
        angles += angles[:1]  # close the loop

        fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))
        fig.patch.set_facecolor('#0a0a0f')
        ax.set_facecolor('#0e0e1e')

        def plot_radar(scores, color, label):
            vals = [scores["health"], scores["career"], scores["wealth"], scores["happiness"]]
            vals += vals[:1]
            ax.plot(angles, vals, 'o-', linewidth=2, color=color, label=label)
            ax.fill(angles, vals, alpha=0.15, color=color)

        plot_radar(scores_c, '#00f5ff', 'Current')
        plot_radar(scores_b, '#39ff14', 'Best Case')
        plot_radar(scores_w, '#ff003c', 'Worst Case')

        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories, color='#aaaacc', fontsize=11)
        ax.set_ylim(0, 100)
        ax.set_yticks([25, 50, 75, 100])
        ax.set_yticklabels(['25', '50', '75', '100'], color='#555577', fontsize=8)
        ax.grid(color='#1a1a3a', linestyle='--', linewidth=0.8)
        ax.spines['polar'].set_color('#1a1a3a')
        ax.tick_params(colors='#aaaacc')

        patches = [
            mpatches.Patch(color='#00f5ff', label='Current'),
            mpatches.Patch(color='#39ff14', label='Best Case'),
            mpatches.Patch(color='#ff003c', label='Worst Case'),
        ]
        ax.legend(handles=patches, loc='upper right', bbox_to_anchor=(1.35, 1.1),
                  facecolor='#0e0e1e', edgecolor='#1a1a3a', labelcolor='#ccccee', fontsize=9)

        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    except Exception:
        # Fallback to bar chart if matplotlib fails
        render_comparison_chart(scores_c, scores_b, scores_w)

def generate_life_timeline(scores_c, scores_b, scores_w):
    import pandas as pd
    
    ages = list(range(20, 41, 2))  # 20 → 40
    
    def simulate_growth(base_score, growth_rate):
        values = []
        current = base_score

        for i in range(len(ages)):
            current = current + (growth_rate * (1 + i * 0.15))  # increasing effect
            current = max(0, min(100, current))
            values.append(current)

        return values

    # Simulate different trajectories
    current_path = simulate_growth(scores_c["overall"], 0.8)
    best_path    = simulate_growth(scores_b["overall"], 2.2)
    worst_path   = simulate_growth(scores_w["overall"], -2.0)

    df = pd.DataFrame({
        "Age": ages,
        "Current Path": current_path,
        "Best Path": best_path,
        "Worst Path": worst_path
    })

    df = df.set_index("Age")
    return df


# ─────────────────────────────────────────────────────────────
# MAIN APP
# ─────────────────────────────────────────────────────────────

def main():

    # ── HERO HEADER ────────────────────────────────────────────
    st.markdown('<div class="hero-title">🔮 FUTURE YOU </div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-sub">Behavior · Habits · Destiny — Your Life, Decoded</div>', unsafe_allow_html=True)

    # Tagline pills
    st.markdown("""
    <div style="text-align:center; margin-bottom:2rem;">
        <span class="info-pill">📊 Deterministic Engine</span>
        <span class="info-pill">🧠 Behavior Modeling</span>
        <span class="info-pill">🚀 3-Scenario Simulation</span>
        <span class="info-pill">🆓 100% Free</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.divider()

    # ── INPUT PANEL ────────────────────────────────────────────
    st.markdown('<div class="section-header">⚙ Input Your Daily Habits</div>', unsafe_allow_html=True)

    col_a, col_b = st.columns([1.2, 1], gap="large")

    with col_a:
        st.markdown("**🌙 Sleep & Recovery**")
        sleep = st.slider("Sleep Hours per night", 0.0, 10.0, 6.5, 0.5,
                          help="Ideal: 7–8 hours. Under 6 = burnout fuel.")

        st.markdown("**📚 Productivity**")
        study = st.slider("Study / Work Hours per day", 0.0, 12.0, 6.0, 0.5,
                          help="Consistent effort is the career unlock.")

        st.markdown("**📱 Screen Time**")
        screen = st.slider("Recreational Screen Time (hrs/day)", 0.0, 12.0, 4.0, 0.5,
                           help="Includes social media, reels, gaming — not study/work.")

    with col_b:
        st.markdown("**🏃 Physical Activity**")
        exercise = st.slider("Exercise Hours per day", 0.0, 3.0, 0.5, 0.25,
                             help="Even 30 mins/day moves the needle hugely.")

        st.markdown("**🤝 Social Life**")
        social = st.slider("Social Interaction (hrs/day)", 0.0, 5.0, 1.5, 0.5,
                           help="Real connections, not just DMs.")

        st.markdown("**💸 Money Habits**")
        spending = st.select_slider(
            "Monthly Spending Level",
            options=["Low", "Medium", "High"],
            value="Medium",
            help="Low = saves actively. High = lifestyle inflation."
        )
        current_inputs = (sleep, study, screen, exercise, social, spending)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.divider()

    # ── SIMULATE BUTTON ────────────────────────────────────────
    btn_col = st.columns([1, 2, 1])[1]
    with btn_col:
        simulate = st.button("🔮  SIMULATE MY FUTURE", use_container_width=True, type="primary")

        # Initialize session state
        if "run_simulation" not in st.session_state:
            st.session_state.run_simulation = False

        if "last_inputs" not in st.session_state:
            st.session_state.last_inputs = current_inputs

        # Detect input change → reset simulation
        if current_inputs != st.session_state.last_inputs:
            st.session_state.run_simulation = False

        # Button click → run simulation + store inputs
        if simulate:
            st.session_state.run_simulation = True
            st.session_state.last_inputs = current_inputs
    if current_inputs != st.session_state.last_inputs:
        st.info("⚙️ Inputs changed — click simulate to update results")

    # ── ALWAYS SHOW RESULTS (or on button press) ───────────────
    # We auto-show on load so the demo always has content visible
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.divider()
    if st.session_state.run_simulation:

        # ── COMPUTE ALL 3 SCENARIOS ────────────────────────────────
        # Current
        scores_c = calculate_scores(sleep, study, screen, exercise, social, spending)
        story_c  = generate_story(scores_c, "current", sleep, study, screen, exercise, social, spending)

        st.markdown(f"""
        <div style="text-align:center; margin: 2rem 0;">
            <div style="font-size:0.8rem; color:#888;">YOUR LIFE SCORE</div>
            <div style="font-size:3.5rem; font-weight:900; color:#00f5ff;">
                {scores_c["overall"]}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Best Case (improved inputs)
        s_b = make_improved(sleep, study, screen, exercise, social, spending)
        scores_b = calculate_scores(*s_b)
        story_b  = generate_story(scores_b, "best", *s_b)

        # Worst Case (degraded inputs)
        s_w = make_worst(sleep, study, screen, exercise, social, spending)
        scores_w = calculate_scores(*s_w)
        story_w  = generate_story(scores_w, "worst", *s_w)

        # Habit summaries (shown in cards)
        def habit_tag(slp, std, scr, exc, soc, spd):
            return f"Sleep {slp}h · Study {std}h · Screen {scr}h · Exercise {exc}h · {spd} Spend"

        summary_c = habit_tag(sleep, study, screen, exercise, social, spending)
        summary_b = habit_tag(*s_b)
        summary_w = habit_tag(*s_w)

        # ── SECTION: SCENARIO CARDS ────────────────────────────────
        tab1, tab2, tab3 = st.tabs(["📊 Current", "🚀 Best", "📉 Worst"])

        with tab1:
            render_scenario("CURRENT",
                            "card-current", "card-title-current",
                            scores_c, story_c, summary_c)

        with tab2:
            render_scenario("BEST",
                            "card-best", "card-title-best",
                            scores_b, story_b, summary_b)

        with tab3:
            render_scenario("WORST",
                            "card-worst", "card-title-worst",
                            scores_w, story_w, summary_w)

        # ── SECTION: COMPARISON CHART ──────────────────────────────
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.divider()
        st.markdown('<div class="section-header">📊 Visual Comparison</div>', unsafe_allow_html=True)

        chart_col, radar_col = st.columns([1.2, 1], gap="large")

        with chart_col:
            st.markdown("**Score Breakdown — All Scenarios**")
            render_comparison_chart(scores_c, scores_b, scores_w)

        with radar_col:
            st.markdown("**Radar — Life Balance View**")
            render_radar(scores_c, scores_b, scores_w)

        st.markdown("<br><br>", unsafe_allow_html=True)
        st.divider()
        st.markdown('<div class="section-header">📈 Life Timeline Projection</div>', unsafe_allow_html=True)

        timeline_df = generate_life_timeline(scores_c, scores_b, scores_w)

        st.markdown("**Your Life Trajectory (Age 20 → 40)**")

        st.line_chart(timeline_df, height=350)
        

        # ⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆

        
        # ── SECTION: SCORE DELTA ───────────────────────────────────
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.divider()
        st.markdown('<div class="section-header">⚡ Improvement Potential</div>', unsafe_allow_html=True)

        delta_cols = st.columns(4)
        metrics = [
            ("❤️ Health",    scores_c["health"],    scores_b["health"]),
            ("💼 Career",    scores_c["career"],    scores_b["career"]),
            ("💰 Wealth",    scores_c["wealth"],    scores_b["wealth"]),
            ("😊 Happiness", scores_c["happiness"], scores_b["happiness"]),
        ]
        for i, (label, current, best) in enumerate(metrics):
            with delta_cols[i]:
                delta = best - current
                delta_str = f"+{delta}" if delta >= 0 else str(delta)
                delta_color = "#39ff14" if delta >= 0 else "#ff003c"
                st.markdown(f"""
                <div style="background:#0e0e1e; border:1px solid #1a1a35; border-radius:10px; padding:1rem; text-align:center;">
                    <div style="font-size:0.75rem; color:#7777aa; letter-spacing:2px;">{label}</div>
                    <div style="font-family:'Orbitron',monospace; font-size:1.4rem; color:#e0e0f0;">{current}</div>
                    <div style="font-size:0.85rem; color:{delta_color}; font-weight:600;">{delta_str} pts if improved</div>
                </div>
                """, unsafe_allow_html=True)

    # ── FOOTER ─────────────────────────────────────────────────
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.divider()
    st.markdown("""
    <div style="text-align:center; color:#333355; font-size:0.78rem; letter-spacing:2px;">
        FUTURE YOU · BEHAVIOR-TO-FUTURE MODELING SYSTEM<br>
        DETERMINISTIC ENGINE · NO AI API · 100% FREE · BUILT WITH STREAMLIT
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()