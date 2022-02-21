@bot.on(admin_cmd(pattern="repo"))
@bot.on(sudo_cmd(pattern="repo", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    Repo = f"[Click Here](https://github.com/kaal0408/Meow2.0)"
    Deploy = f"[Click Here](https://dashboard.heroku.com/new?template=https%3A%2F%2Fgithub.com%2kaal0408%2FMeow2.0)"
    await edit_or_reply(
        event, f"**Meow 2.0 userbot Repo:** {Repo}\n\n**Deploy Now:** {Deploy}"
    )
