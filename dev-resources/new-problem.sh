#!/bin/zsh

set -euo pipefail

SHORT_OPTS="hvp:f"
LONG_OPTS="help,verbose,problem-path:,force"

PARSED_OPTS=$(getopt \
              --options $SHORT_OPTS \
              --longoptions $LONG_OPTS \
              --name "$0" -- "$@")
[[ $? -ne 0 ]] && print -P "%F{red}Error from $(where getopt).%f" >&2 && exit 1
eval set -- "$PARSED_OPTS"

verbose=0
problem_path=""
force_flag=""
DIR=$(dirname $(realpath $0))

function print_help {
  echo "Usage: $0 [-h|--help] [-v|--verbose] [-p|--problem-path <path>]"
  echo ""
  echo "Options:"
  echo "  -h, --help            Show this help message and exit"
  echo "  -v, --verbose         Enable verbose output"
  echo "  -p, --problem-path    Specify the problem path (mandatory)"
  echo "                        The last segment is expected to start with problem_xx."
  echo "  -f, --force           Overwrite file if exists"
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    -h | --help)
      print_help()
      exit 0
      ;;
    -v | --verbose)
      (( verbose = verbose + 1 ))
      shift
      ;;
    -p | --problem-path)
      problem_path="$2"
      shift 2
      ;;
    -f | --force)
      force_flag=1
      shift
      ;;
    --)
      shift
      break
      ;;
    *)
      echo "Unknown option: $1"
      exit 1
      ;;
  esac
done

if [[ -z "$problem_path" ]]; then
  echo "Error: --problem-path is required"
  print_help
  exit 1
fi

if [[ "$problem_path" =~ ^[a-z0-9_/]+/([a-z0-9_]+/problem_[0-9]+)_.*$ ]]; then
  git_branch=${match[1]}
else
  echo "Error: --problem-path is expected to contain a folder and problem_ prefix."
  print_help
  exit 1
fi

verbose_flag=""
if [[ $verbose -gt 0 ]]; then
  verbose_flag="-$(printf '%*s' "$verbose" | tr ' ' 'v')"
fi

src_paths=(
  "${DIR}/problem_template.py"
  "${DIR}/problem_template.org"
  "${DIR}/problem_template_test_.py"
)
dest_paths=(
  "${DIR}/../src/${problem_path}.py"
  "${DIR}/../src/${problem_path}.org"
  "${DIR}/../tests/${problem_path}_test.py"
)

function print_test {
  pywatch_command="poetry run ptw -- -- $verbose_flag \\\\
  $(realpath --relative-to ${DIR}/.. $dest_paths[1]) \\\\
  $(realpath --relative-to ${DIR}/.. $dest_paths[3])"

  echo "You may watch the tests for this specific problem with:"
  echo ""
  print -P "%F{green}${pywatch_command}%f"
}

for i in {1..3}; do
  src=${src_paths[$i]}
  mkdir -p ${dest_paths[$i]%/*}
  dest=$(realpath "${dest_paths[$i]}")

  if [[ -e $dest && $force_flag -eq 0 ]]; then
    print -P "%F{red}File $dest already exists.%f" >&2
    if [[ -n ${verbose} ]]; then
      echo ""
      print_help
    fi
    echo ""
    print_test

    exit 1
  fi

  cp $verbose_flag "$src" "$dest"
  temp_file=$(mktemp)
  mustache_data=$(cat <<EOF
  {
    'xxx_filename': '${problem_path##*/}',
    'xxx_module_path': '${problem_path//\//.}'
  }
EOF
  )
  poetry run chevron --data <(echo $mustache_data) $dest > $temp_file
  mv $verbose_flag $temp_file $dest
  if [[ -n ${verbose} ]]; then
    echo "Copied $src to $dest"
  fi
done

echo ""
echo "Creating git branch ${git_branch}"
git switch -c "${git_branch}"

echo ""
print -P "%F{green}Success.%f"
echo ""
print_test
