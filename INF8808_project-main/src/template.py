'''
    Contains the template to use in the data visualization.
'''
import plotly.graph_objects as go
import plotly.io as pio


THEME = {
    'font_family': 'Roboto',
    'accent_font_family': 'Roboto Slab',
    'dark_color': '#2A2B2E',
    'label_font_size': 14,
    'label_background_color': '#ffffff',
}

# Custom theme for the app
def create_custom_theme():
    '''
        Adds a new layout template to pio's templates.

        The template sets the font color and
        font to the values defined above in
        the THEME dictionary, using the dark
        color.

        Also, sets the hover label to have a
        background color and font size
        as defined for the label in the THEME dictionary.
        The hover label's font color is the same
        as the theme's overall font color. 
        
    '''
    # Generate template described above
    pio.templates['custom'] = dict(
        layout = go.Layout(
        title_font = dict(family = THEME['font_family'],
            color = THEME['dark_color']),
        font = dict(family = THEME['font_family'],
            color= THEME['dark_color']),
        plot_bgcolor = THEME['plot_background_color'], 
        hoverlabel = dict(font=
                        dict(family = THEME['font_family'],
                             size = THEME['label_font_size'],
                             color = THEME['dark_color']),
                             bgcolor = THEME['label_background_color'])))

def set_default_theme():
    '''
        Sets the default theme to be a combination of the
        'plotly_white' theme and our custom theme.
    '''
    # TODO : Set default theme
    fig = go.Figure()

    fig.update_layout(
        template = pio.templates['plotly_white'],
        dragmode = False,
        barmode = 'relative'
    )
    
    # Setting the tempalte
    pio.templates.default = 'plotly_white+custom'
    fig.update_layout(template = pio.templates.default)


# Hover template for Viz1
def get_hover_template_viz1():
    '''
        Sets the template for the hover tooltips in the visualization 1 in page2.

        Contains two labels, followed by their corresponding
        value, separated by a colon : Date, and New Tap Number.

        The labels are bold. The values are normal weight.
    '''
    hovertemplate = '<b>Date</b>: %{x}<br /><b>New Tap Number</b>: %{y} <br /><extra></extra>'
    return hovertemplate

# Hover template for Viz2
def get_hover_template_viz2():
    '''
        Sets the template for the hover tooltips in the visualization 2.

        Contains two labels, followed by their corresponding
        value : Number of Change, and Tap position.
    '''
    hovertemplate = '<b>Number of Change: %{x} <br><b>Tap position: %{y}<extra></extra>'
    return hovertemplate

# Hover template for Viz3
def get_viz3_hover_template():
    '''
        Sets the template for the hover tooltips in the Viz 3.
        Contains four labels, followed by their corresponding
        value, separated by a colon : Max_loadcurrent, Max_PowerLoss, Max_EnergyLoss, and Max_CircCurrent.
            
        The labels are bold. The values are normal weight.
    '''
    return """<span style='font-weight:bold'><b>    Max_LoadCurrent</b></span><span style='font-weight:normal'> : %{customdata[0]} <br /></span>
    <span style='font-weight:bold'><b>Max_PowerLoss</b></span><span style='font-weight:normal'> : %{customdata[1]} <br /></span>
    <span style='font-weight:bold'><b>Max_EnergyLoss</b></span><span style='font-weight:normal'> : %{customdata[2]} <br /></span>
    <span style='font-weight:bold'><b>Max_CircCurrent</b></span><span style='font-weight:normal'> : %{customdata[3]} <br /></span>"""

# Hover template for Viz8
def get_hover_template_viz8():
    """
        Sets the template for the hover tooltips in the visualization 2.

        Contains two labels, followed by their corresponding
        value : Year and Circulatiing current.
    """
    hovertemplate = '<b>Year: %{x} <br><b>Circulatiing current: %{y:.4f}(kA) <extra></extra>'
    return hovertemplate

# Hover template for Viz9
def get_hover_template_viz9_barchart():
    """
        Sets the template for the hover tooltips in the visualization 9.

        Contains two labels, followed by their corresponding value
    """
    hovertemplate = '<b>Time (hour): %{x}<br><b>Maximum load current: %{y} (KA) <extra></extra>'
    return hovertemplate

# Hover template for bar chart in the dashboard
def get_hover_template_dash_barchart():
    """
        Sets the template for the hover tooltips in the bar chart displayed in the dashboard.

        Contains two labels, followed by their corresponding value
    """
    hovertemplate = '<b>Tap: %{x}<br><b>Power Loss: %{y}<extra></extra>'
    return hovertemplate



# Hover template for tap history plot in dashboard
def get_tap_history_hover_template():
    '''
        Sets the template for the hover tooltips in the tap recent history plot in dashboard.

        Contains three labels, followed by their corresponding
        value, separated by a colon : Tap Number, Date, and Time.

        The labels are bold. The values are normal weight.
    '''
    # Return the hover template
    hovertemplate = """<b>Tap Number</b>: %{y} <br /><b>Date</b>: %{customdata} <br /><b>Time</b>: %{x[1]} <br /><extra></extra>"""
    return hovertemplate

# Hover template for Viz6
def get_dumbbell_hover_template():
    '''
        Sets the template for the hover tooltips in the dumbbell plot.

        Contains four labels, followed by their corresponding
        value, separated by a colon : Date, Time, Tap Operation Time, and Tap Power Loss Time.
            - Tap Operation Time and Tap Power Loss Time are fomatted with three decimal points 
            
        The labels are bold. The values are normal weight.
    '''
    # Return the hover template
    hovertemplate = '<b>Date:</b> %{customdata[0]}'+'<br><b>Time:</b> %{x[1]}'+'<br><b>Tap Operation Time:</b> %{customdata[1]:.3f}'+'<br><b>Tap Power Loss Time:</b> %{customdata[2]:.3f}'+'<br><extra></extra>'
    return hovertemplate

# Hover template for Viz7 (Power loss)
def get_viz7_2_hover_template():
    '''
        Sets the template for the hover tooltips in the Viz 7 (power loss plot).
        values are rounded to the two decimal places.
    '''
    return """<b>Day: %{x}<br><b>Power Loss: %{y:.2f} <extra></extra>"""

# Hover template for Viz7 (Energy loss)
def get_viz7_1_hover_template():
    '''
        Sets the template for the hover tooltips in the Viz 7 (Energy loss plot).
        values are rounded to the three decimal places.
    '''
    return """<b>Day: %{x}<br><b>Energy Loss: %{y:.3f} <extra></extra>"""
