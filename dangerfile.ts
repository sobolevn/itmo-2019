import { message, fail, danger } from 'danger'

// Critical:
console.log(JSON.stringify(danger.github))
console.log(JSON.stringify(danger.github.base))
console.log(JSON.stringify(danger.github.head))

message(JSON.stringify(danger.github))
message(JSON.stringify(danger.github.base))
message(JSON.stringify(danger.github.head))

if (danger.github.base.ref !== 'master') {
  fail('We only accept PRs to `master` branch.')
}

if (danger.github.head.ref.match(/homework-\d+/)) {
  fail('Your branch should be named `homework-${HOMEWORK_NUMBER}`.')
}
