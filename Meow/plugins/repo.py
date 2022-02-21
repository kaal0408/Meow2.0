@bot.on(admin_cmd(pattern="repo"))
@bot.on(sudo_cmd(pattern="repo", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    Repo = f"[Click Here](https://github.com/Copycat-izz-opp/CopyCat_Spam_Bot)"
    Deploy = f"[Click Here](https://dashboard.heroku.com/new?template=https%3A%2F%2Fgithub.com%2FYukkiBot%2FYukkiXdeploy)"
    await edit_or_reply(
        event, f"**CopyCat Spam Bot Repo:** {Repo}\n\n**Deploy Now:** {Deploy}"
    )
