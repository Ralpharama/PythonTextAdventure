from location import Location

locs = {}

# Ilano terrace
locs["ILANOTERRACE"] = Location(
    "ILANOTERRACE",
    "Ilano terrace",
    "In summer months the central square of the mall is converted into a terassi, think a small kiosk serving drinks, tables, chairs, parasols.",
    "NORTHOFSQUARE","EASTOFSQUARE","SOUTHOFSQUARE","WESTOFSQUARE"
    )

# South of the square
locs["SOUTHOFSQUARE"] = Location(
    "SOUTHOFSQUARE",
    "South of the square",
    "Near the supermarket.",
    "ILANOTERRACE"
    )

