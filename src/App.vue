<script setup>
import { ref } from 'vue'

// Board state - 9x9 array of numbers (0 = empty)
const board = ref(Array(81).fill(0))

// Cage data structure: {cells: number[], sum: number, color: string}
const cages = ref([])

// Available cage colors
const cageColors = [
  '#FFB3BA', // Light pink
  '#BAFFC9', // Light green
  '#BAE1FF', // Light blue
  '#FFFFBA', // Light yellow
  '#E6B3FF', // Light purple
  '#FFD1BA', // Light orange
  '#B3FFE6', // Light mint
  '#FFB3E6', // Light magenta
  '#D1BAFF', // Light periwinkle
]

// Currently selected cells for creating a cage
const selectedCells = ref([])

// Current cage sum
const cageSum = ref(0)

// Track mouse state
const isMouseDown = ref(false)
const lastToggledCell = ref(null)

// Handle mouse events
const onMouseDown = (index) => {
  isMouseDown.value = true
  toggleCell(index)
}

const onMouseEnter = (index) => {
  if (isMouseDown.value && lastToggledCell.value !== index) {
    toggleCell(index)
  }
}

const onMouseUp = () => {
  isMouseDown.value = false
  lastToggledCell.value = null
}

// Toggle cell selection
const toggleCell = (index) => {
  const selectedIndex = selectedCells.value.indexOf(index)
  if (selectedIndex === -1) {
    selectedCells.value.push(index)
  } else {
    selectedCells.value.splice(selectedIndex, 1)
  }
  lastToggledCell.value = index
}

// Get adjacent cell indices
const getAdjacentCells = (index) => {
  const row = Math.floor(index / 9)
  const col = index % 9
  const adjacent = []

  // Check left
  if (col > 0) adjacent.push(index - 1)
  // Check right
  if (col < 8) adjacent.push(index + 1)
  // Check up
  if (row > 0) adjacent.push(index - 9)
  // Check down
  if (row < 8) adjacent.push(index + 9)

  return adjacent
}

// Create a cage from selected cells
const createCage = () => {
  if (selectedCells.value.length > 0) {
    // Find available color that's not used by adjacent cages
    let availableColor = null
    for (const color of cageColors) {
      let isColorValid = true
      for (const cell of selectedCells.value) {
        const adjacentCells = getAdjacentCells(cell)
        for (const adjCell of adjacentCells) {
          const adjCage = cages.value.find(c => c.cells.includes(adjCell))
          if (adjCage && adjCage.color === color) {
            isColorValid = false
            break
          }
        }
        if (!isColorValid) break
      }
      if (isColorValid) {
        availableColor = color
        break
      }
    }

    cages.value.push({
      cells: [...selectedCells.value],
      sum: cageSum.value,
      color: availableColor || cageColors[0] // Fallback to first color if no valid color found
    })
    selectedCells.value = []
  }
}

// Delete a cage containing the given cell
const deleteCage = (index) => {
  const cageIndex = cages.value.findIndex(cage => cage.cells.includes(index))
  if (cageIndex !== -1) {
    cages.value.splice(cageIndex, 1)
  }
}

// Get cell color for a cell
const getCellColor = (index) => {
  if (selectedCells.value.includes(index)) {
    return '#ffff00' // Highlight selected cells in yellow
  }
  const cage = cages.value.find(c => c.cells.includes(index))
  return cage ? cage.color : '#f0f0f0'
}

// Get cage sum for a cell
const getCageSum = (index) => {
  const cage = cages.value.find(c => c.cells.includes(index))
  // Only show sum on the first cell of the cage
  if (cage && cage.cells[0] === index) {
    return cage.sum
  }
  return null
}

// Update cell value
const updateCell = (index, value) => {
  board.value[index] = value
}

// Check if a number is valid in a given position
const isValidMove = (index, num) => {
  const row = Math.floor(index / 9)
  const col = index % 9
  const boxRow = Math.floor(row / 3) * 3
  const boxCol = Math.floor(col / 3) * 3

  // Check row
  for (let c = 0; c < 9; c++) {
    if (c !== col && board.value[row * 9 + c] === num) return false
  }

  // Check column
  for (let r = 0; r < 9; r++) {
    if (r !== row && board.value[r * 9 + col] === num) return false
  }

  // Check 3x3 box
  for (let r = 0; r < 3; r++) {
    for (let c = 0; c < 3; c++) {
      const checkIndex = (boxRow + r) * 9 + (boxCol + c)
      if (checkIndex !== index && board.value[checkIndex] === num) return false
    }
  }

  // Check cage sum and remaining possibilities
  const cage = cages.value.find(c => c.cells.includes(index))
  if (cage) {
    // Calculate current sum and remaining empty cells
    let currentSum = 0
    let emptyCells = []
    for (const cellIndex of cage.cells) {
      if (cellIndex === index) {
        currentSum += num
      } else if (board.value[cellIndex] === 0) {
        emptyCells.push(cellIndex)
      } else {
        currentSum += board.value[cellIndex]
      }
    }

    // If sum already exceeds target, invalid
    if (currentSum > cage.sum) return false

    // If no empty cells left, must equal target sum
    if (emptyCells.length === 0 && currentSum !== cage.sum) return false

    // Check if remaining sum is possible with remaining cells
    const remainingSum = cage.sum - currentSum
    if (emptyCells.length > 0) {
      // Minimum possible sum (using 1s)
      const minPossible = emptyCells.length
      // Maximum possible sum (using 9s)
      const maxPossible = emptyCells.length * 9

      if (remainingSum < minPossible || remainingSum > maxPossible) return false
    }
  }

  return true
}

// Find best empty cell to try next
const findBestEmptyCell = () => {
  let bestCell = -1
  let minPossibilities = 10

  for (let i = 0; i < 81; i++) {
    if (board.value[i] === 0) {
      let possibilities = 0
      for (let num = 1; num <= 9; num++) {
        if (isValidMove(i, num)) possibilities++
      }
      if (possibilities < minPossibilities) {
        minPossibilities = possibilities
        bestCell = i
      }
      // Optimization: if we found a cell with only one possibility, use it
      if (minPossibilities === 1) break
    }
  }
  return bestCell
}

// Solve the puzzle using optimized backtracking
const solve = () => {
  const emptyCell = findBestEmptyCell()
  if (emptyCell === -1) return true // Puzzle completed

  // Get the cage containing this cell if any
  const cage = cages.value.find(c => c.cells.includes(emptyCell))

  // Try numbers in an optimized order based on cage constraints
  let numbers = []
  if (cage) {
    // Calculate remaining sum needed
    const currentSum = cage.cells.reduce((sum, cell) =>
      sum + (cell === emptyCell ? 0 : board.value[cell]), 0)
    const remainingSum = cage.sum - currentSum

    // Filter possible numbers based on remaining sum
    numbers = Array.from({ length: 9 }, (_, i) => i + 1)
      .filter(n => n <= remainingSum)
  } else {
    numbers = Array.from({ length: 9 }, (_, i) => i + 1)
  }

  for (const num of numbers) {
    if (isValidMove(emptyCell, num)) {
      board.value[emptyCell] = num
      if (solve()) return true
      board.value[emptyCell] = 0 // Backtrack
    }
  }
  return false
}

// Generate constraints for export
const generateBasicConstraints = () => {
  const constraints = []

  // Value range constraints for each cell
  for (let i = 0; i < 81; i++) {
    constraints.push(`board[${i}] >= 1`)
    constraints.push(`board[${i}] <= 9`)
  }

  // Row constraints
  for (let row = 0; row < 9; row++) {
    const cells = []
    for (let col = 0; col < 9; col++) {
      cells.push(`board[${row * 9 + col}]`)
    }
    constraints.push(`AllDifferent(${cells.join(', ')})`)
  }

  // Column constraints
  for (let col = 0; col < 9; col++) {
    const cells = []
    for (let row = 0; row < 9; row++) {
      cells.push(`board[${row * 9 + col}]`)
    }
    constraints.push(`AllDifferent(${cells.join(', ')})`)
  }

  // 3x3 box constraints
  for (let boxRow = 0; boxRow < 3; boxRow++) {
    for (let boxCol = 0; boxCol < 3; boxCol++) {
      const cells = []
      for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
          const row = boxRow * 3 + i
          const col = boxCol * 3 + j
          cells.push(`board[${row * 9 + col}]`)
        }
      }
      constraints.push(`AllDifferent(${cells.join(', ')})`)
    }
  }

  return constraints
}

const pythonSolverCodeTemplate = `
from z3 import Int, Solver

solver = Solver()

board = [ Int('b%d' % i) for i in range(81) ]

def AllDifferent(*cells):
    for i in cells:
        for j in cells:
            if i is not j:
                solver.add(i != j)
    return True

# PUT CONSTRAINTS HERE

print(solver.check())
m = solver.model()
for i, b in enumerate(board):
    print(m[b],end='\\n' if i % 9 == 8 else '')
`

// Export all constraints
const exportConstraints = () => {
  const basicConstraints = generateBasicConstraints()
  const killerConstraints = cages.value.map(cage => {
    const cells = cage.cells.map(i => `board[${i}]`).join('+')
    return `${cells} == ${cage.sum}`
  })

  const allConstraints = pythonSolverCodeTemplate.trim().replace(
    '# PUT CONSTRAINTS HERE',
    [
      '# Basic Sudoku constraints',
      ...(basicConstraints.map(c => `solver.add(${c})`)),
      '',
      '# Killer cage constraints',
      ...(killerConstraints.map(c => `solver.add(${c})`))
    ].join('\n')
  )

  return allConstraints
}

// Import constraints and restore state
const importConstraints = (text) => {
  // Clear current state
  board.value = Array(81).fill(0)
  cages.value = []

  const lines = text.split('\n')
  let currentSection = ''

  for (const line of lines) {
    if (line.startsWith('#')) {
      currentSection = line
      continue
    }

    if (!line.trim() || !line.startsWith('solver.add')) continue

    if (currentSection.includes('Killer cage')) {
      // Parse killer cage constraint
      const match = line.match(/solver\.add\((.*?)\s*==\s*(\d+)\)/)
      if (!match) continue

      const [_, cells, sum] = match
      const cellIndices = cells.split('+').map(cell => {
        const indexMatch = cell.match(/board\[(\d+)\]/)
        return parseInt(indexMatch[1])
      })

      // Create new cage
      cages.value.push({
        cells: cellIndices,
        sum: parseInt(sum),
        color: cageColors[cages.value.length % cageColors.length]
      })
    }
  }
}

// Handle textarea click to copy constraints
const copyConstraints = async () => {
  const textarea = document.querySelector('.constraints')
  textarea.select()
  // Only copy if HTTPS
  if (window.location.protocol === 'https:') {
    try {
      await navigator.clipboard.writeText(textarea.value)
    } catch (err) {
      console.error('Failed to copy:', err)
    }
  }
}
</script>

<template lang="pug">
.killer-sudoku
  .controls
    input(
      type="number"
      placeholder="Cage sum"
      v-model="cageSum"
      @keyup.enter="createCage"
    )
    button(@click="createCage") Create Cage
    button(@click="solve") Solve
    textarea.constraints(
      :value="exportConstraints()"
      rows="3"
      placeholder="Constraints will appear here"
      @input="importConstraints($event.target.value)"
      @click="copyConstraints"
    )

  .board(@mouseup="onMouseUp" @mouseleave="onMouseUp")
    .cell(
      v-for="(cell, index) in board"
      :key="index"
      :style="{ backgroundColor: getCellColor(index) }"
      @mousedown="onMouseDown(index)"
      @mouseenter="onMouseEnter(index)"
      @contextmenu.prevent="deleteCage(index)"
    )
      .cage-sum(v-if="getCageSum(index)") {{ getCageSum(index) }}
      input(
        type="number"
        v-model="board[index]"
        min="1"
        max="9"
        @input="updateCell(index, $event.target.value)"
        @dragstart.prevent
      )
</template>

<style lang="sass" scoped>
.killer-sudoku
  display: flex
  flex-direction: column
  gap: 20px
  padding: 20px

.board
  display: grid
  grid-template-columns: repeat(9, 1fr)
  gap: 1px
  background: #000
  width: 900px
  height: 900px
  user-select: none

.cell
  background: #f0f0f0
  display: flex
  align-items: center
  justify-content: center
  position: relative

  .cage-sum
    position: absolute
    top: 5px
    left: 5px
    font-size: 12px
    font-weight: bold

  input
    width: 90%
    height: 90%
    border: none
    background: transparent
    text-align: center
    font-size: 20px

    &::-webkit-outer-spin-button,
    &::-webkit-inner-spin-button
      -webkit-appearance: none
      margin: 0

.controls
  display: flex
  gap: 10px

  button
    padding: 8px 16px

  .constraints
    flex: 1
    font-family: monospace
    padding: 8px
</style>
