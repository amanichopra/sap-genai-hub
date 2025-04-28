from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from gen_ai_hub.orchestration.service import OrchestrationService, OrchestrationConfig
from gen_ai_hub.orchestration.models.message import SystemMessage, UserMessage
from gen_ai_hub.orchestration.models.template import Template, TemplateValue
from gen_ai_hub.orchestration.models.llm import LLM
import os
import json
from dotenv import load_dotenv

load_dotenv()

# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# function to get summary using orchestration service
def get_summary_using_gen_ai_hub(text, llm):
    summary = 'Summary here...'
    return summary

# Layout of the app
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Text Summarizer", className="text-center my-4"), width=12)
    ]),
    dbc.Row([
        dbc.Col(dcc.Textarea(
            id='input-text',
            placeholder='Enter text here...',
            style={'width': '100%', 'height': 150}
        ), width=12)
    ]),
    dbc.Row([
        dbc.Col(dcc.Dropdown(
            id='llm-dropdown',
            options=[
                {'label': "Gemini 1.5 Flash", 'value': 'gemini-1.5-flash'},
                {'label': "GPT-4o Mini", 'value': 'gpt-4o-mini'},
                {'label': "Anthropic Claude 3 Opus", 'value': 'anthropic--claude-3-opus'},
                {'label': "Mistralai Mixtral 8x7B Instruct v0.1", 'value': 'mistralai--mixtral-8x7b-instruct-v01'}
            ],
            placeholder="Select LLM",
            style={'width': '100%'}
        ), width=12)
    ]),
    dbc.Row([
        dbc.Col(
            dbc.Button("Generate Summary", id='generate-btn', color="primary", className="my-3"),
            width=12, className="text-center"
        )
    ]),
    dbc.Row([
        dbc.Col(dcc.Loading(
            id="loading-summary",
            type="circle",  # Spinner type: "circle", "dot", or "default"
            children=dcc.Textarea(
                id='output-summary',
                placeholder='Summary will appear here...',
                style={'width': '100%', 'height': 150},
                readOnly=True
            )
        ), width=12)
    ])
], fluid=True)

# Callback to generate summary
@app.callback(
    Output('output-summary', 'value'),
    Input('generate-btn', 'n_clicks'),
    State('input-text', 'value'),
    State('llm-dropdown', 'value')
)
def generate_summary(n_clicks, input_text, llm_value):
    if n_clicks and input_text and llm_value:
        # Simple logic to include LLM choice in the summary
        summary = get_summary_using_gen_ai_hub(input_text, llm_value)
        return summary
    elif n_clicks:
        return "Please provide text and select an LLM."
    return ""

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
