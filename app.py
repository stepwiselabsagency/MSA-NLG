from flask import Flask, render_template, request, send_file
import pandas as pd
from utils.utils import (
    generate_extra_data,
    generate_table_data,
    generate_bar_data,
    get_data,
    save_docx
)

app = Flask(__name__)

def _get_fields(prefix: str, keys: list[str], defaults: list[str]) -> tuple[str, ...]:
    """
    Retrieve a series of form fields, apply defaults if missing or empty.
    """
    values: list[str] = []
    for key, default in zip(keys, defaults):
        raw = request.form.get(f"{prefix}{key}", "").strip()
        values.append(raw if raw else default)
    return tuple(values)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    # Read uploaded CSV
    uploaded = request.files.get("file")
    filename = uploaded.filename
    df = pd.read_csv(uploaded)

    # Generate metadata and chart data
    (team1, team2, goals1, goals2,
     club, year, tournament, date_str) = generate_extra_data(df, filename)
    title = f"{team1} Vs {team2}"
    table_json = generate_table_data(df)
    bar_json = generate_bar_data(df)

    # Toggle and option settings
    selected_option = request.form.get("option", "")
    arena_toggled = "arena" in request.form

    # Prepare default values
    name_defaults_1 = ["team 1 player 1", "team 1 player 2", "team 1 player 3", "team 1 player 4"]
    name_defaults_2 = ["team 2 player 1", "team 2 player 2", "team 2 player 3", "team 2 player 4"]
    goal_defaults = ["-99"] * 4

    # Collect form inputs
    team1_names = _get_fields("field", ["1", "2", "3", "4"], name_defaults_1)
    team1_goals = _get_fields("field", ["5", "6", "7", "8"], goal_defaults)
    team2_names = _get_fields("field", ["11", "22", "33", "44"], name_defaults_2)
    team2_goals = _get_fields("field", ["55", "66", "77", "88"], goal_defaults)

    # Adjust for arena toggle (omit fourth player if toggled)
    if arena_toggled:
        fields_tuple_1 = team1_names[:3] + team1_goals[:3]
        fields_tuple_2 = team2_names[:3] + team2_goals[:3]
    else:
        fields_tuple_1 = team1_names + team1_goals
        fields_tuple_2 = team2_names + team2_goals

    # Handicap fields
    hg_winning = request.form.get("handicapgoalswinning", "0") or "0"
    hg_losing = request.form.get("handicapgoalslosing", "0") or "0"
    handicap_tuple = (hg_winning, hg_losing)

    # Process and enrich data
    processed = get_data(
        df,
        filename,
        fields_tuple_1,
        fields_tuple_2,
        handicap_tuple,
        toggle_button=selected_option,
        arena_toggled=arena_toggled,
    )
    processed["link"] = request.form.get("link", "")

    # Generate and return output
    save_docx(processed)

    if "word" in request.form:
        return send_file(
            "temp.docx",
            as_attachment=True,
            download_name=f"{title}.docx",
        )
    if "upload" in request.form:
        upload_json_to_drive("temp.docx")
        return "File Uploaded Successfully"

    return "Invalid request"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)