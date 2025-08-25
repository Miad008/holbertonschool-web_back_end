export default function cleanSet(set, startString) {
  const filtered = [...set].filter(value => value.startsWith(startString));
  const trimmed = filtered.map(value => value.slice(startString.length));
  return trimmed.join('-');
}
