# itmo-2019

[![Github Actions CI](https://github.com/sobolevn/itmo-2019/workflows/build/badge.svg)](https://github.com/sobolevn/itmo-2019/actions)
[![Gitter](https://badges.gitter.im/itmo-2019/community.svg)](https://gitter.im/itmo-2019/community)

This package contains all the source code and lecture files.
Any questions? Ask them in our [`gitter room`](https://gitter.im/itmo-2019/community).


## Requirements

You will need:

- [`python3.7`](https://github.com/pyenv/pyenv)
- [`poetry`](https://github.com/sdispater/poetry)
- `pycharm` or [`vscode`](https://github.com/sobolevn/dotfiles)


## Marks

We track our progress in [Google Forms]().


## Homework submission

All our homeworks are submitted via Pull Requests.
This is very important, since we learn [how to maintain](https://opensource.guide/how-to-contribute/) an [Open Source Software](https://en.wikipedia.org/wiki/Open-source_software) repository.
There are a lot of tricky parts and manual labour, which we are mastering.

### Process

1. [Create a custom fork](https://help.github.com/en/articles/fork-a-repo) to work locally
2. Name your branch as `homework-${HOMEWORK_NUMBER}` where `${HOMEWORK_NUMBER}` is `1`, `2`, `3`, `4`, ...
3. [Create a Pull Request](https://help.github.com/en/desktop/contributing-to-projects/creating-a-pull-request) with files under `students/${YOUR_GTIHUB_ACCOUNT}/${HOMEWORK_NUMBER}`. Do not touch anything else
4. Use the correct [Pull Request template](https://github.com/sobolevn/itmo-2019/blob/master/.github/pull_request_template.md) (it should be suggested automatically by GitHub)
5. Make sure that [all checkboxes are checked](https://github.com/stilliard/github-task-list-completed) in the Pull Request template
4. Make sure that [CI works](https://github.blog/2019-08-08-github-actions-now-supports-ci-cd/)
5. Pass a [code review](https://github.com/features/code-review/)
6. Send a link to [`gitter`](https://gitter.im/itmo-2019/community) before the deadline
7. Done!

### Deadline

We have a strict deadline for your homework: each `Thursday at 18:00 UTC+03:00`
Any submission after that time is not counted. But appreciated.


## Final score

```python
final_mark = 0.4 * final_exam + 0.6 * (0.5 * homework + 0.5 * tests)
```

### Criteria

| Score  | Result |
|--------|--------|
| >= 40% |    3   |
| >= 60% |    4   |
| >= 80% |    5   |


## Timetable

|   | Start |  End  |
|---|:-----:|:-----:|
| 1 | 10:00 | 11:30 |
| 2 | 11:40 | 13:10 |


## License

MIT.
